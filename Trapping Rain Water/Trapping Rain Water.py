class Solution:
    def trap(self, height: List[int]) -> int:
        stack = list()

        for i in range(len(height)):
            while stack and stack[-1][0] < height[i]:
                stack.pop()

            stack.append((height[i], i))

        left = 0
        out = 0

        for i in range(len(height)):
            while stack and stack[0][1] == i:
                stack.pop(0)
            # print(stack,left, height)
            if stack and stack[0][0] > height[i] and left > height[i]:
                curr = min(left,stack[0][0])
                out += curr-height[i]
            if height[i] > left:
                left = height[i]

        return out 
