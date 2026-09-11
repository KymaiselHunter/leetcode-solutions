class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = dict()
        left = 0
        out = 0

        for i, c in enumerate(s):
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

            currMax = max(d, key=d.get)
            
            # length of current substring - amount of non max chars
            currSubstring = (i + 1) - left
            while currSubstring - d[currMax] > k:
                leftChar = s[left]
                d[leftChar] -= 1
                left += 1

                if d[leftChar] == 0:
                    d.pop(leftChar)

                currSubstring = (i + 1) - left
            
            out = max(out, currSubstring)

        return out