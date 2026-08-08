class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        sm = min(nums)
        bg = max(nums)

        nums = set(nums)
        out = list()

        for i in range(sm, bg):
            if i not in nums:
                out.append(i)

        return out