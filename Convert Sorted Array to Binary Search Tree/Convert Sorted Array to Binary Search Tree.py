# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recur(nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return

            it = len(nums)//2
            # print(it, nums[it])
            newNode = TreeNode(nums[it])

            newNode.left = recur(nums[0:it])
            newNode.right = recur(nums[it+1::])

            return newNode

        return recur(nums)
