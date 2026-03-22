class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target: 
            return True

        def rotate(mat):
            out = [[-1 for i in range(len(mat))] for j in range(len(mat))]

            for i in range(len(mat)):
                for j in range(len(mat)):
                    out[i][j] = mat[j][len(mat)-1-i]

            return out
        
        for i in range(3):
            mat = rotate(mat)

            if mat == target:
                return True

        return False