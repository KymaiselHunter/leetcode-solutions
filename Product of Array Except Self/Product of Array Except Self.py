class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[i] for i in range(len(nums))]
        right = [nums[i] for i in range(len(nums))]

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i] 
            right[-i - 1] = right[-i] * nums[-i-1]

        # print(left)
        # print(right)
        out = [1 for i in range(len(nums))]

        for i in range(len(out)):
            if i > 0:
                out[i] *= left[i-1]

            if i < len(out)-1:
                out[i] *= right[i+1]

        return out