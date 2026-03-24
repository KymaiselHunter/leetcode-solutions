class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        pre = 1
        suf = 1

        rowCount, colCount = len(grid), len(grid[0])
        pMatrix = [[None for j in range(colCount)] for i in range(rowCount)]
        sMatrix = [[None for j in range(colCount)] for i in range(rowCount)]

        for i in range(rowCount):
            for j in range(colCount):
                pMatrix[i][j] = pre
                sMatrix[rowCount - 1 - i][colCount - 1 - j] = suf

                pre *= grid[i][j]
                suf *= grid[rowCount - 1 - i][colCount - 1 - j]
        # print(product)

        out = [[pMatrix[i][j] * sMatrix[i][j] % 12345 for j in range(colCount)] for i in range(rowCount)]

        return out
