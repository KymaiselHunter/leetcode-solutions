class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0] 
        biggest = heapq.nlargest(2, stones)

        return 0 if biggest[0]==biggest[1] else abs(biggest[0]-biggest[1])