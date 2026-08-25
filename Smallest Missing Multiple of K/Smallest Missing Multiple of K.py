class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        check = set(nums)

        for i in range(k, 101 + k, k):
            if not i in check:
                return i

        return -1