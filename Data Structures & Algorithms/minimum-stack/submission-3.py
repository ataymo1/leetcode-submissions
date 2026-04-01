class MinStack:

    def __init__(self):
        self.stack = [] # (val, min_val)


        

    def push(self, val: int) -> None:
        stack = self.stack
        if stack and stack[-1][1] < val:
            stack.append((val, stack[-1][1]))
        else:
            stack.append((val, val))

    def pop(self) -> None:
        stack = self.stack
        stack.pop()
        
    def top(self) -> int:
        stack = self.stack
        return stack[-1][0]

    def getMin(self) -> int:
        stack = self.stack
        return stack[-1][1]    
