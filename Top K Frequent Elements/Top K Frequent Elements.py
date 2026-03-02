class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        # print(sorted(c.items(), key=lambda item: item[1]))
        # top = sorted(c.items(), key=lambda item: item[1], reverse=True)

        return heapq.nlargest(k, c.keys() , key=lambda item: c[item])

        # # print(heap)

        # return [top[i][0] for i in range(k)]