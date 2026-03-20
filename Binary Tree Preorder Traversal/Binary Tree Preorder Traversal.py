# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def pre(node: Optional[TreeNode]):
            if not node:
                return

            nonlocal out
            out.append(node.val)
            pre(node.left)
            pre(node.right)

        pre(root)

        return out
