class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        out = 0
        cost = sorted(cost)[::-1]

        for i in range(len(cost)):
            if (i + 1) % 3 == 0:
                continue

            out += cost[i]
        return out
            