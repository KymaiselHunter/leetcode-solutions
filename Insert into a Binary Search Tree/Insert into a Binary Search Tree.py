# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root

        out = root
        
        prev = None
        while root:
            if root.val > val:
                prev = root
                root = root.left
                continue
            prev = root
            root = root.right
        
        root = TreeNode(val)
        
        if prev.val > val:
            prev.left = root
        else:
            prev.right = root

        return out
        
