class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        out = 0 

        for key in sorted(c.keys()):

            if key+1 in c:
                out = max(out, c[key] + c[key+1])

        return out
            
