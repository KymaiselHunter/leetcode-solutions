class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        out = 0
        for index, num in enumerate(nums):
            out += index * num

        total = sum(nums)
    
        prev = out
        for index in range(len(nums)-1, 0, -1):
            curr = prev

            curr += total
            curr -= len(nums) * nums[index]

            out = max(out,curr)
            prev = curr
            # print(curr, index)

        return out
