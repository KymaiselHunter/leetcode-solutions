class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()

        for i, n in enumerate(nums):
            if target - n in cache:
                return [cache[target-n], i]

            cache[n] = i

        return [-1,-1]