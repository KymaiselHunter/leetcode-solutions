class Solution:
    def removeStars(self, s: str) -> str:
        stack = list()

        for c in s:
            if not c == '*':
                stack.append(c)
                continue

            if stack:
                stack.pop(-1)

        return "".join(stack)
            