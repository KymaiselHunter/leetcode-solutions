class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        out = 0

        while n:
            out += n % 10
            n //= 10

        return out