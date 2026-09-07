class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        d = dict()
        out = 0

        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
                out = max(out, i - left + 1)
                continue
            
            left = d[c] + 1
            d[c] = i

            out = max(out, i - left + 1)

        return out