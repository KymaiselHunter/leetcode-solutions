class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        out = 0
        curr = 0

        for num in gain:
            curr += num

            out = max(out,curr)

        return out