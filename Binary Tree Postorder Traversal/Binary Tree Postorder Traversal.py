# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recur(node: TreeNode, out: list):
            if not node:
                return

            recur(node.left, out)
            recur(node.right, out)
            out.append(node.val)

        out = list()
        recur(root, out)
        return out