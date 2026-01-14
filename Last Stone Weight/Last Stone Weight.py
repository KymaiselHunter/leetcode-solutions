class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            res = -abs(stone1-stone2)
            heapq.heappush(stones,res)

        if len(stones) == 1:
            return -stones[0]
        return 0
