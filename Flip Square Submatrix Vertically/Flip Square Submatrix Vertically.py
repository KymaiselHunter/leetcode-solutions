class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for j in range(y, y+k):
            print(j)
            for i in range((k)//2):
                grid[x+i][j], grid[(x+k-1)-i][j] = grid[(x+k-1)-i][j], grid[x+i][j]

        return grid