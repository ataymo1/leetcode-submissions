class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0
        

    def next(self, price: int) -> int:
        self.day += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if not self.stack:
            self.stack.append((price, self.day))
            return self.day
        else:
            self.stack.append((price, self.day))
            return self.day - self.stack[-2][1]

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)