class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp = [[(0,0) for j in range(len(grid[0]))] for i in range(len(grid))]
        dp[len(grid)-1][len(grid[0])-1] = (grid[len(grid)-1][len(grid[0])-1],grid[len(grid)-1][len(grid[0])-1])
        # print(dp)
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i >= len(grid)-1 and j >= len(grid[i]) - 1:
                    continue

                currMax = currMin = None
                # print(i,j)
                if j < len(grid[i]) - 1:
                    rightMax = grid[i][j] * dp[i][j+1][0]
                    rightMin = grid[i][j] * dp[i][j+1][1]

                    currMax = max(rightMax, rightMin)
                    currMin = min(rightMax, rightMin)

                if i < len(grid) - 1:
                    downMax = grid[i][j] * dp[i+1][j][0]
                    downMin = grid[i][j] * dp[i+1][j][1]

                    if not currMax:
                        currMax = max(downMax, downMin)
                        currMin = min(downMax, downMin)
                    else:
                        currMax = max(currMax, downMax, downMin)
                        currMin = min(currMin, downMax, downMin)

                dp[i][j] = (currMax, currMin)

        out = max(dp[0][0][0], dp[0][0][1])
        # print(dp)
        return out if out >= 0 else -1