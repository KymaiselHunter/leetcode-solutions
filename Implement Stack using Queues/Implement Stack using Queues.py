class MyStack:

    def __init__(self):
        self.q1 = list()
        self.q2 = None
        self.size = 0

    def push(self, x: int) -> None:
        if self.empty():
            self.q2 = x
            self.size += 1
            return
        
        self.q1.append(x)

        for i in range(self.size):
            if self.q2:
                self.q1.append(self.q2)
                self.q2 = None

            self.q2 = self.q1.pop(0)
        
        self.size += 1


    def pop(self) -> int:
        if self.empty():
            return None

        self.size -= 1

        out = self.q2
        self.q2 = None

        if not self.empty() and not self.q2:
            self.q2 = self.q1[0]
            self.q1.pop(0)

        return out

    def top(self) -> int:
        if self.empty():
            return None

        return self.q2

    def empty(self) -> bool:
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()