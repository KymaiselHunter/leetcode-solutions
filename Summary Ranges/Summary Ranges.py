class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = list()

        if not nums:
            return out
        
        left = nums[0]
        right = nums[0]

        for i in range(1,len(nums)):
            if nums[i] - 1 == right:
                right = nums[i]
                continue

            if left == right:
                out.append(str(left))
            else:
                out.append(str(left)+"->"+str(right))
            left = nums[i]
            right = nums[i]

        if left == right:
            out.append(str(left))
        else:
            out.append(str(left)+"->"+str(right))
        left = nums[i]
        right = nums[i]

        return out

            