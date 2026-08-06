class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        it = n

        for i in range(n, 100 + 1):
            curr = 1
            it = i

            while it:
                curr *= it % 10
                it //= 10

            if curr % t == 0:
                return i

        return -1