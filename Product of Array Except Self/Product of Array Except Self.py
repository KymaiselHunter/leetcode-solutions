class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        suf = [1]

        for i in range(1,len(nums)):
            pre.append(pre[i-1]*nums[i-1])
            suf.insert(0,suf[-i]*nums[-i])

        return [pre[i] * suf[i] for i in range(len(nums))]