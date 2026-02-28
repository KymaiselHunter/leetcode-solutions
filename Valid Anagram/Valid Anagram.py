class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = set(s)
        tSet = set(t)

        if tSet == sSet:
            return True

        return False