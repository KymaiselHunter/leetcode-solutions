class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        numsSize = len(nums)

        bfs = []

        for index, num in enumerate(nums):
            # tuple represents:
            # current index, total sum, index to multiply by
            bfs.append((index, 0, 0))

        out = 0

        while bfs:
            curr = bfs.pop(0)

            index, total, position = curr

            if position >= numsSize:
                out = max(out, total)
                continue

            bfs.append(((index + 1) % numsSize, total + position * nums[index], position + 1))

        return out