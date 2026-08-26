class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        out = ""
        stack = list()

        for i, c in enumerate(s):
            if c == '1':
                stack.append(i)
            
        while len(stack) >= k:
            if not out:
                out = s[stack[0]:stack[k-1]+1]
                
            out = max(out, s[stack[0]:stack[k-1]+1])
            
            stack.pop(0)

        return out