class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = dict()
        out = 0
        curr = 0

        for index, num in enumerate(nums):
            curr += num

            if curr == k:
                out += 1

            if curr - k in d:
                out += d[curr-k] 

            if curr in d:
                d[curr] += 1
            else:
                d[curr] = 1

        return out