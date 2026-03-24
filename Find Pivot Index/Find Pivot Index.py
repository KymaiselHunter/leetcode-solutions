class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightWindow = 0
        
        for i in range(len(nums)):
            rightWindow += nums[i]

        leftWindow = 0 
        for i in range(0,len(nums)):
            # print(i, leftWindow, rightWindow)
            rightWindow -= nums[i]
            if leftWindow == rightWindow:
                return i
            leftWindow += nums[i]

        return -1