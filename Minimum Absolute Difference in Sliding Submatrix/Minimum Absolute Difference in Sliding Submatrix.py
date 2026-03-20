class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        out = list()

        for i in range(len(grid)-k +1):
            curr = list()

            for j in range(len(grid[i])-k+1):
                nums = set()
                for m in range(i,i+k):
                    for n in range(j,j+k):
                        nums.add(grid[m][n])

                if len(nums) <= 1:
                    curr.append(0)
                    continue
                
                nums = sorted(list(nums))
                
                diff = abs(nums[0]-nums[1])

                for p in range(2,len(nums)):
                    diff = min(abs(nums[p-1]-nums[p]), diff)
                curr.append(diff)


            out.append(curr)

        return out