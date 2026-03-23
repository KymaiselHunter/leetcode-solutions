class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        curr = 0

        for i in range(k):
            curr += nums[right]
            right += 1
       
        out = curr / k

        while right < len(nums):
            curr -= nums[left]
            curr += nums[right]

            out = max(out, curr/k)

            left += 1
            right += 1

        return out