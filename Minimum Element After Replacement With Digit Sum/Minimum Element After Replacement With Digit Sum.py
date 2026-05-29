class Solution:
    def minElement(self, nums: List[int]) -> int:
        out = -1

        for num in nums:
            curr = num
            dSum = 0

            while curr:
                dSum += curr % 10
                curr //= 10

            if out == -1:
                out = dSum
                continue

            out = min(out, dSum)

        return out