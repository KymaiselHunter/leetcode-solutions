class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        left = start 
        right = start 

        while left >= 0 or right < len(nums):
            if left >= 0:
                if nums[left] == target:
                    return abs(left - start)
                left -= 1
                
            if right < len(nums):
                if nums[right] == target:
                    return abs(right - start)
                right += 1
        return -1