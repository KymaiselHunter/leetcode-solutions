class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        path = set()

        DIRS = ((1,0), (-1,0), (0,1), (0,-1))

        def inBounds(row: int, col: int) -> bool:
            if row < 0 or col < 0:
                return False
            nonlocal grid
            if row >= len(grid) or col >= len(grid[0]):
                return False

            return True

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                start = (row,col)
                def recur(row: int, col: int, pDir: Tuple[int][int]) -> bool:
                    if not inBounds(row, col):
                        return False

                    nonlocal start
                    nonlocal grid
                    if grid[row][col] != grid[start[0]][start[1]]:
                        return False

                    nonlocal path
                    if (row, col) in path:
                        return True
                    
                    path.add((row,col))
                    for dr, dc in DIRS:
                        if (-dr, -dc) == pDir:
                            continue
                        if recur(row + dr, col + dc, (dr,dc)):
                            return True
                    path.remove((row,col))
                    

                if recur(row, col, (0,0)):
                    return True
        return False
