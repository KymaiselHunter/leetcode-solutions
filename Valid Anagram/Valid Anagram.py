class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = sorted(s)
        tSet = sorted(t)

        if tSet == sSet:
            return True

        return False