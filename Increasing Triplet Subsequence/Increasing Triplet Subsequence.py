class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        biggest = []
        for j in range(len(nums)-1,0,-1):
            if not biggest:
                biggest.insert(0, nums[j])
                continue
            curr = max(nums[j], biggest[0])
            biggest.insert(0, curr)

        left = nums[0]
        for i in range(1, len(nums)):
            if left < nums[i] and nums[i] < biggest[0]:
                return True
            
            if left > nums[i]:
                left = nums[i]
            biggest.pop(0)

        return False
                
            

