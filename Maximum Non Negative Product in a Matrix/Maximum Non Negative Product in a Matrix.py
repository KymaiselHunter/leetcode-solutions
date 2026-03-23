class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp = [[(0,0) for j in range(len(grid[0]))] for i in range(len(grid))]
        
        # print(dp)
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i >= len(grid)-1 and j >= len(grid[i]) - 1:
                    start = grid[i][j]
                    dp[len(grid)-1][len(grid[0])-1] = (start, start, True if start == 0 else False)
                    continue

                currMax = currMin = None
                zero = grid[i][j] == 0
                # print(i,j)
                if j < len(grid[i]) - 1:
                    rightMax = grid[i][j] * dp[i][j+1][0]
                    rightMin = grid[i][j] * dp[i][j+1][1]

                    currMax = max(rightMax, rightMin)
                    currMin = min(rightMax, rightMin)

                    if dp[i][j+1][2]:
                        zero = True

                if i < len(grid) - 1:
                    downMax = grid[i][j] * dp[i+1][j][0]
                    downMin = grid[i][j] * dp[i+1][j][1]

                    if not currMax:
                        currMax = max(downMax, downMin)
                        currMin = min(downMax, downMin)
                    else:
                        currMax = max(currMax, downMax, downMin)
                        currMin = min(currMin, downMax, downMin)

                    if dp[i+1][j][2]:
                        zero = True

                dp[i][j] = (currMax, currMin, zero)

        out = max(dp[0][0][0], dp[0][0][1])
        # print(dp)
        return out % (pow(10,9) + 7) if out >= 0 else -1 if not dp[0][0][2] else 0