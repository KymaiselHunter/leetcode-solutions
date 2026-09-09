class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # print(rows, cols)
        rows = list(rows)
        cols = list(cols)

        for row in rows:
            for j in range(len(matrix[row])):
                matrix[row][j] = 0

        for col in cols:
            for j in range(len(matrix)):
                matrix[j][col] = 0