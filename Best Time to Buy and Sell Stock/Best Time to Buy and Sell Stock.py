class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        big = prices[-1]
        
        for i in range(len(prices)-1,-1,-1):
            big = max(big, prices[i])
            out = max(out, big - prices[i])

        return out