class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = nums
        self.queue.sort()
        self.index = k

    def add(self, val: int) -> int:
        self.queue.append(val)
        self.queue.sort()
        # print(self.queue)
        return self.queue[-self.index]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)