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
                    right = mid - 1
                    continue
                left = mid + 1

            return left if arr[left] == target else -1
        # if not rotated
        # regular binary search 
        if nums[0] < nums[-1]:
            return binarySearch(nums, 0, len(nums)-1, target)

        # if target is greater than right value
        # we check left side
        # binary search for a right value that is above or equal to target
        # if not found, -1
        if target > nums[-1]:
            left = 0
            right = len(nums)-1

            while left < right:
                mid = (right - left) // 2 + left

                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    right = mid
                    break
                if nums[mid] < nums[0]:
                    right = mid - 1
                    continue
                left = mid + 1
            return binarySearch(nums, 0, right, target)

        # if target is less than right value
        # we check right side
        # binary search for a left value that is below or equal to target
        # if not found, -1
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (right - left) // 2 + left
            # print(mid, nums[mid])

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid
                break
            if nums[mid] > nums[-1]:
                left = mid + 1
                continue
            right = mid - 1
        # print(left, nums[left])
        return binarySearch(nums, left, len(nums)-1, target)

