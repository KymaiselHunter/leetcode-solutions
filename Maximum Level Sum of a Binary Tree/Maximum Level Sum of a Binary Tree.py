# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        output = None
        max = None
        breadth = [root]

        while breadth:
            sum = 0
            for i in range(len(breadth)):
                curr = breadth[0]
                sum += curr.val
                
                if curr.left:
                    breadth.append(curr.left)

                if curr.right:
                    breadth.append(curr.right)

                breadth.pop(0)
            print(level, sum)
            if not output or not max or sum > max:
                output = level
                max = sum
            level += 1

        return output

