class SmallestInfiniteSet:

    def __init__(self):
        self.h = list()
        self.hc = set()
        self.n = 1

    def popSmallest(self) -> int:
        if not self.h:
            out = self.n
            self.n += 1
            return out
        
        out = heapq.heappop(self.h)
        self.hc.remove(out)
        return out

    def addBack(self, num: int) -> None:
        if num >= self.n or num in self.hc:
            return
        heapq.heappush(self.h, num)
        self.hc.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)