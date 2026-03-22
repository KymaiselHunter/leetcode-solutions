class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most = -1

        for c in candies:
            most = max(most, c)

        out = [True for i in range(len(candies))]

        for i in range(len(candies)):
            if candies[i] + extraCandies < most:
                out[i] = False

        return out