class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(i, total, included):
            if i == len(nums):
                return included if total == target else -1
            if (i, total, included) in dp:
                return dp[(i,total,included)]
            
            dp[(i, total, included)] = backtrack(i+1, total, included)
            dp[(i, total, included+1)] = backtrack(i+1, total ^ nums[i], included+1)
        
        backtrack(0,0,0)
        # print(dp)
        # print(max(v for v in dp.values() if v is not None))
        # print(max(dp, key=lambda x: x[2]))
        included = max(v for v in dp.values() if v is not None)
        return len(nums) - included if included > 0 else included 