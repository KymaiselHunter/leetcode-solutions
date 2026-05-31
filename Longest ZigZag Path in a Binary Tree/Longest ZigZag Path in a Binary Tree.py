# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        out = 0
        
        # dir: 0 = left, 1 = right, 2 = start
        def recur(node, dr):
            if not node:
                return 0
            curr = 0
            nonlocal out

            if dr == 0:
                out = max(out, recur(node.left, 0))

                curr = 1 + recur(node.right, 1)
                out = max(out, curr)
                return curr
            elif dr == 1:
                out = max(out, recur(node.right, 1))

                curr = 1 + recur(node.left, 0)
                out = max(out, curr)
                return curr

            return max(recur(node.right, 1), recur(node.left, 0), out)

        return recur(root, 2)