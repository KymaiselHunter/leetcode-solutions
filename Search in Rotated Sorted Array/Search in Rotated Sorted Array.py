class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        def binarySearch(arr: List[int], left: int, right: int, target: int):
            while left < right:
                mid = (right - left) // 2 + left

                if arr[mid] == target:
                    return mid
                if arr[mid] > target:
                    right = mid -1
                    continue
                left = mid + 1

            return -1
        # regular binary search
        if nums[0] < nums[-1]:
            return binarySearch(nums, 0, len(nums)-1, target)

        # if target is greater than right value
