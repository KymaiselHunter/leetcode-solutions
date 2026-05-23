class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        cache = set()
        cache.add(nums[0])
        out = set()

        for i in range(1,len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j]) * -1 in cache:
                    new = [nums[i], nums[j], (nums[i] + nums[j]) * -1]
                    new = tuple(sorted(new))
                    out.add(new)
            cache.add(nums[i])

        out = [list(item) for item in out]

        return out