class Solution:
    def check(self, nums: List[int]) -> bool:
        inc = True
        prev = -1
        small = float('inf')
        
        for num in nums:
            if num < prev:
                if not inc:
                    return False
                inc = False
                
            if inc:
                small = min(small, num)
            elif num > small:
                return False
                
            prev = num
        return True