class FreqStack:

    def __init__(self):
        self.heap = []
        self.values = defaultdict(int)
        self.count = 0

    def push(self, val: int) -> None:
        self.values[val] += 1
        self.count += 1
        heapq.heappush(self.heap, tuple((-self.values[val], -self.count, val)))
        
    def pop(self) -> int:
        freq, count, val = heapq.heappop(self.heap)
        self.values[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()