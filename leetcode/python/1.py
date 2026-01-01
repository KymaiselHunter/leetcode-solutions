class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()

        for index, num in enumerate(nums):
            # print(index, num)
            if target - num in cache:
                return [cache[target-num], index]
            cache[num] = index

        # print(cache)
        return [-1,-1]