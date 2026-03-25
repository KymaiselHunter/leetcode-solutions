class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        totalSum = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                totalSum += grid[i][j]

        # print("totalSum:", totalSum)

        shrink = totalSum
        grow = 0
        for i in range(len(grid)-1):
            for j in range(len(grid[i])):
                grow += grid[i][j]
                shrink -= grid[i][j]

            if shrink == grow:
                # print("horizontal at", i)
                return True
        
        shrink = totalSum
        grow = 0
        for j in range(len(grid[0])-1):
            for i in range(len(grid)):
                grow += grid[i][j]
                shrink -= grid[i][j]
            
            # print(shrink,grow)
            if shrink == grow:
                # print("vertical at", j)
                return True

        return False

        