class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        out = -1

        while left < right:
            # print(left,right, right-left * min(height[left],height[right]))
            out = max((right-left) * min(height[left],height[right]), out)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return out