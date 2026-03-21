class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        for i in range(len(t)):
            if left >= len(s):
                return True
            if t[i] == s[left]:
                left += 1

        if left >= len(s):
            return True
        return False