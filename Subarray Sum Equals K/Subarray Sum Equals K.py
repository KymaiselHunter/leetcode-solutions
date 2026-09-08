class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = list()
        curr = 0
        for num in nums:
            curr += num
            prefix.append(curr)

        count = dict()
        out = 0

        for index, num in enumerate(prefix):
            out += (num == k)
            out += count[num-k] if num-k in count else 0

            count[num] = 1 if not num in count else count[num] + 1

        return out