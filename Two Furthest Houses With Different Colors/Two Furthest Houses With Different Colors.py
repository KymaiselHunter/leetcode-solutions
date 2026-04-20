class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        out = 0

        for i in range(len(colors)):
            right = len(colors)-1

            while i < right and colors[i] == colors[right]:
                right -= 1

            out = max(out, right - i)
        return out