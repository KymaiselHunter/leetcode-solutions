class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        discounts = [-x for x in discounts]; heapq.heapify(discounts)
        prices = [-x for x in prices]; heapq.heapify(prices)

        out = 0

        while prices:
            if discounts:
                out += prices[0] * -1 * (100 - discounts[0] * -1) / 100
                heapq.heappop(discounts)
                heapq.heappop(prices)
                continue

            out += prices[0] * -1
            heapq.heappop(prices)

        return out