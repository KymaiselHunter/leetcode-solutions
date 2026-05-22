class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        left = 0 
        right = len(nums) -1 
        while left < right:
            mid = (right - left) // 2 + left

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                # target is in right half
                if nums[mid] < nums[-1]:
                    right = mid - 1
                    continue
                # target is in left half
                left = mid + 1
                continue                

            #else if nums[mid] < target

            # target is in right
            if nums[mid] < nums[-1]: 
                left = mid + 1
                continue
            right = mid - 1

        return left if nums[left] == target else -1
        