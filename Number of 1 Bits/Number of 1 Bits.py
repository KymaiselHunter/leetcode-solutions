class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        while n:
            if n % 2 == 1:
                out += 1
            n//=2
        return out