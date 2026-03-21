# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def recur(node, key):
            if not node:
                return node
            # print(node.val)

            if node.val < key:
                node.right = recur(node.right, key)
                return node

            if node.val > key:
                node.left = recur(node.left, key)
                return node

            if not node.right or not node.left:
                # if no children
                if not node.right and not node.left:
                    return None
                # if one child
                return node.left if node.left else node.right
            
            # if both child
            prev = node
            it = node.right

            while it.left:
                prev = it
                it = it.left
            
            if prev == node:
                # print('kawa')
                node.val = it.val
                node.right = it.right
                return node
            # print('k3awa')
            node.val = it.val
            prev.left = it.right
            return node

        return recur(root, key)
            
                     



        