class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        out = [-1,-1]

        check = [False for i in range(len(nums))]

        for num in nums:
            if check[num-1] == True:
                out[0] = num
            check[num-1] = True 

        for i in range(len(check)):
            if not check[i]:
                out[1] = i + 1
                break

        return out