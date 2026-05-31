class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        st = sorted(nums)
        c = dict()
        for i, num in enumerate(st):
            if num not in c:
                c[num] = i

        out = [0 for i in range(len(nums))]

        for i in range(len(out)):
            out[i] = c[nums[i]]

        # print(st)
        # print(c)

        return out