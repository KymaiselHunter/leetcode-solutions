class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (right - left) // 2 + left
            # print(left, mid, right)
            if nums[mid] <= nums[right]:
                right = mid
                continue

            left = mid + 1
        # print(left, right, nums[left])
        return nums[left]