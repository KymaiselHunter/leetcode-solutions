class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        pre = 1
        MOD = 12345
        rowCount, colCount = len(grid), len(grid[0])
        out = [[1 for j in range(colCount)] for i in range(rowCount)]

        for i in range(rowCount):
            for j in range(colCount):
                out[i][j] = pre

                pre = (pre * (grid[i][j] % MOD)) % MOD
        
        pre = 1
        for i in range(rowCount -1, -1, -1):
            for j in range(colCount -1, -1, -1):
                out[i][j] = (out[i][j] * pre) % MOD
                pre = (pre * (grid[i][j] % MOD)) % MOD

        return out
