class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def recur(
            row: int, 
            col: int, 
            right: int, 
            down: int
            ) -> List[int]: 
            if row >= down or col >= right:
                return []
            
            currRow = row
            currCol = col
            
            out = [matrix[currRow][currCol]]

            while currCol < right - 1:
                currCol += 1
                out.append(matrix[currRow][currCol])

            if row == down - 1:
                return out

            while currRow < down - 1: 
                currRow += 1
                out.append(matrix[currRow][currCol])

            if col == right - 1:
                return out

            while currCol > col:
                currCol -= 1
                out.append(matrix[currRow][currCol])
            
            while currRow > row + 1: 
                currRow -= 1
                out.append(matrix[currRow][currCol])

            return out + recur(currRow, currCol + 1, right - 1, down - 1)

        return recur(0,0, len(matrix[0]), len(matrix))
        