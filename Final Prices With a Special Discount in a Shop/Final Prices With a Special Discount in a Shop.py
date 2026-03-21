class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        mp = defaultdict(lambda: 0)
        stack = list()

        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                mp[stack.pop()] = p
            stack.append(i)

        return [prices[i]-mp[i] for i in range(len(prices))]
