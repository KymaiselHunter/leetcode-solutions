# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        out = 0

        # first return values, second return node count
        def recur(node: TreeNode) -> (int, int):
            if not node:
                return (0, 0)

            left = recur(node.left)
            right = recur(node.right)

            currSum = node.val + left[0] + right[0]
            currCount = 1 + left[1] + right[1]

            if int(currSum / currCount) == node.val:
                nonlocal out
                out += 1
                # print(node.val)


            return (currSum, currCount)

        recur(root)
        return out
