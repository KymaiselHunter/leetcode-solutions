# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = 0

        def count(node):
            if not node:
                return 0
            return node.val + count(node.left) + count(node.right)

        total = count(root)
        output = -1

        def recur(node):
            if not node:
                return 0 
            
            it = recur(node.left) + recur(node.right)
            val = node.val + it
            nonlocal output
            nonlocal total
            # print(total, val, (total - val)*val)
            output = max((total - val)*val, output) 

            return val

        # print(total)
        recur(root)
        return output % (pow(10,9) + 7)
