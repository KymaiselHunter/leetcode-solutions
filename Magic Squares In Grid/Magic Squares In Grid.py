class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3  or len(grid[0]) < 3:
            return 0

        counter = 0

        for i in range(len(grid)-2):
            for j in range(len(grid[i])-2):
                invalid = False
                num = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                for k in range(1,3):
                    if grid[k+i][j] + grid[k+i][j+1] + grid[k+i][j+2] != num:
                        invalid = True
                        break
                if invalid:
                    continue
                for k in range(3):
                    if grid[i][k+j] + grid[i+1][k+j] + grid[i+2][k+j] != num:
                        invalid = True
                        break
                if invalid:
                    continue
                if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != num:
                    invalid = True
                    break
                if invalid:
                    continue
                if grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2] != num:
                    invalid = True
                    break
                if invalid:
                    continue
                # if i == 0 and j == 0: 
                #     print('huh')

                cache = set()
                for k in range(i, i+3):
                    for l in range(j,j+3):
                        if grid[k][l] in cache:
                            invalid = True
                            break
                        
                        cache.add(grid[k][l])
                    if invalid == True:
                        break
                if invalid:
                    continue
                counter += 1

        return counter

        