class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = list()

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)

        for i in range(len(zeros)):
            bound = zeros[i+1] if i < len(zeros)-1 else len(nums)
            
            for j in range(zeros[i]+1, bound):
                nums[j-(i+1)] = nums[j]
        
        for i in range(len(nums) - len(zeros) , len(nums)):
            nums[i] = 0