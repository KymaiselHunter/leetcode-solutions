class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        out = 0
        for num in nums:
            if num == 1:
                c += 1
            else:
                c = 0
            out = max(out, c)
        return out
            