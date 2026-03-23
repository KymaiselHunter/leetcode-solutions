# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        out1 = list()
        out2 = list()

        def recur(node, out):
            if not node:
                return

            if not node.left and not node.right:
                out.append(node.val)
                return

            recur(node.left, out)
            recur(node.right, out)

        recur(root1, out1)
        recur(root2, out2)

        # print(out1,out2)
        return out1 == out2