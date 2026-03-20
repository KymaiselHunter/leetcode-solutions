class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        small = val
        if self.getMin() and self.getMin() < small:
            small = self.getMin()
        self.stack.append((val, small))
        print('push', val, self.stack)

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()