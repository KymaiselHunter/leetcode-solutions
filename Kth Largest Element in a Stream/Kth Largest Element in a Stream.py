class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = nums
        heapq.heapify(self.queue)
        self.index = k
        while len(self.queue) > k:
            heapq.heappop(self.queue)

    def add(self, val: int) -> int:
        heapq.heappush(self.queue, val)
        heapq.heappop(self.queue)
        # print(self.queue)
        return self.queue[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)