class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        cache = set()
        cache.add(nums[0])
        out = list()

        for i in range(1,len(nums)):
            skip = set()
            for j in range(i+1,len(nums)):
                if (nums[i], nums[j]) in skip:
                    continue
                if (nums[i] + nums[j]) * -1 in cache:
                    new = [(nums[i] + nums[j]) * -1, nums[i], nums[j]]
                    out.append(new)
                    skip.add((nums[i], nums[j]))
            cache.add(nums[i])


        return out