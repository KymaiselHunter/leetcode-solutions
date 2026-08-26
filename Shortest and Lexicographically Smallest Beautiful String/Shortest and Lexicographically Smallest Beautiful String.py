class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        out = ""
        stack = list()

        for i, c in enumerate(s):
            if c == '1':
                stack.append(i)
            
        while len(stack) >= k:
            curr = s[stack[0]:stack[k-1]+1]
            if not out:
                out = curr
            elif len(curr) == len(out):
                out = min(out, s[stack[0]:stack[k-1]+1])
            else:
                out = out if len(out) < len(curr) else curr
            
            stack.pop(0)

        return out