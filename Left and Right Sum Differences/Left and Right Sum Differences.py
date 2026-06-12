class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0 for i in range(len(nums))]
        right = [0 for i in range(len(nums))]


        for i in range(1, len(nums)):
            left[i] = left[i-1] + nums[i-1]
            right[len(nums) - 1 - i] = right[len(nums) - i] + nums[len(nums) - i]

        # print(left,right)

        for i in range(len(left)):
            left[i] = abs(left[i] - right[i])

        return left