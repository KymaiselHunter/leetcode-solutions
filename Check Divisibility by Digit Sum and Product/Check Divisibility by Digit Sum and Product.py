class Solution:
    def checkDivisibility(self, n: int) -> bool:
        add = 0
        mult = 1
        it = n

        while it:
            add += it % 10
            mult *= it % 10

            it //= 10

        return n % (mult + add) == 0