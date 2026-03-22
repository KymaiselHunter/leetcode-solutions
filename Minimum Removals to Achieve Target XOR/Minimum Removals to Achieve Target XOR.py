class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(i, total, included):
            print(i, total, included)
            if (i, total, included) in dp:
                print(i, total, included,"are you fucking ")
                return dp[(i,total,included)]
            if i == len(nums):
                dp[(i,total,included)] = included if total == target else -1#, dp[(i,total,included)] if dp[(i,total,included)] else -1)
                return dp[(i,total,included)]
            
            ignore = backtrack(i+1, total, included)
            # dp[(i, total, included)] = ignore
            take = backtrack(i+1, total ^ nums[i], included+1)
            # dp[(i, total, included+1)] = take
            dp[(i, total, included)] = max(take, ignore)
            return dp[(i, total, included)]
        
        res=backtrack(0,0,0)
        # print(dp)
        # print(max(v for v in dp.values() if v is not None))
        # # print(max(dp, key=lambda x: x[2]))
        # included = max(v for v in dp.values() if v is not None)
        return len(nums) - res if res > -1 else res