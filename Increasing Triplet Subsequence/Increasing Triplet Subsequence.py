class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        biggest = [-1 for j in range(len(nums))]
        for j in range(len(nums)-1,-1,-1):
            if j == len(nums)-1:
                biggest[j] = nums[j]
                continue
            curr = max(nums[j], biggest[0])
            biggest[j]=curr

        left = nums[0]
        for i in range(1, len(nums)-1):
            if left < nums[i] and nums[i] < biggest[i+1]:
                return True
            
            if left > nums[i]:
                left = nums[i]
            # biggest.pop(0)

        return False
                
            

