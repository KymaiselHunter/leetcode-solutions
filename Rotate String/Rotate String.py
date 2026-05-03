class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        
        for i in range(len(goal)):
            invalid = False
            for j in range(len(s)):
                if s[j] != goal[(i+j)%len(s)]:
                    invalid = True
                    break
            if invalid:
                continue
            return True

        return False