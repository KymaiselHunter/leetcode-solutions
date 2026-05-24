class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        c = defaultdict(int)
        out = list()

        for num in nums:
            # print(c[num])
            if c[num] >= k:
                continue
            c[num] += 1
            out.append(num)

        return out
        