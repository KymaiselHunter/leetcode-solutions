class Solution:
    def minOperations(self, s: str) -> int:
        out = 0

        ones = 0
        for c in s:
            if c == '1':
                ones += 1

        return min(abs(len(s)//2 - ones), abs((len(s)//2) - (len(s)-ones)))