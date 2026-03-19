# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        bfs=[root]

        while bfs:
            # test =""
            # for i in bfs:
            #     test += str(i.val) + " "
            
            # print(test)

            for i in range(len(bfs)//2):
                if not bfs[i] and not bfs[len(bfs)-1-i]:
                    continue

                if not bfs[i] or not bfs[len(bfs)-1-i]:
                    return False

                if bfs[i].val != bfs[len(bfs)-1-i].val:
                    return False
            
            for i in range(len(bfs)):
                if not bfs[0]: 
                    bfs.pop(0)
                    continue
                
                bfs.append(bfs[0].left)
                bfs.append(bfs[0].right)

                bfs.pop(0)

        return True