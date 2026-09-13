class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        out = [[-1 for i in range(n)] for j in range(n)]

        def recur(
            row: int,
            col: int,
            right: int,
            down: int,
            it: int
        ):
            if row >= down or col >= right:
                return
            
            currRow = row
            currCol = col

            out[currRow][currCol] = it
            it += 1

            while currCol < right - 1:
                currCol += 1
                out[currRow][currCol] = it
                it += 1
            
            if row == down - 1:
                return
            
            while currRow < down-1:
                currRow += 1
                out[currRow][currCol] = it
                it += 1

            if col == right - 1:
                return

            while currCol > col:
                currCol -= 1
                out[currRow][currCol] = it
                it += 1

            while currRow > row + 1:
                currRow -= 1
                out[currRow][currCol] = it
                it += 1

            recur(currRow, currCol + 1, right - 1, down - 1, it)

        recur(0,0, len(out[0]), len(out), 1)
        return out