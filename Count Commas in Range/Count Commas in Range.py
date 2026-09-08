class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        small = n % 1000
        big = n // 1000

        return (1000 * (big - 1)) + (small + 1)