# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(node):
            if not node:
                return None, -1
            
            leftNode, leftDepth = recur(node.left)
            rightNode, rightDepth = recur(node.right)

            # if leftNode and rightNode:
            #     print(leftNode.val, leftDepth, rightNode.val, rightDepth)
            if leftDepth == rightDepth:
                if leftDepth == -1:
                    return node, 0
                
                return node, leftDepth + 1

            if leftDepth > rightDepth:
                return leftNode, leftDepth + 1

            return rightNode, rightDepth + 1

        outputNode, outputValue = recur(root)

        return outputNode
            
        