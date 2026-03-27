class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k = k % len(mat[0])
        rotMat = copy.deepcopy(mat)
        for rot in range(k):
            for row in range(len(mat)):
                even = row % 2 == 0

                if even:
                    rotMat[row].append(rotMat[row].pop(0))
                else:
                    rotMat[row].insert(0, rotMat[row].pop(-1))

        print(rotMat)
        print(mat)
        if mat == rotMat:
            return True

        return False