class Solution:
    def trap(self, height: List[int]) -> int:
        stack = list()

        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                stack.pop()

            stack.append(i)

        left = 0
        out = 0

        for i in range(len(height)):
            while stack and stack[0]<=i:
                stack.pop(0)
            # print(stack,left, height)
            if stack and height[stack[0]] > height[i] and left > height[i]:
                curr = min(left,height[stack[0]])
                out += curr-height[i]
                # print(i, curr-height[i], stack)
            if height[i] > left:
                left = height[i]

        return out 
