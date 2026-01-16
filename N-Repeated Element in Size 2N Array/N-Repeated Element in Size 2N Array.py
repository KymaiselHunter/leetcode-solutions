class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        cache = set()
        for num in nums:
            if num in cache: 
                return num
            cache.add(num)

        return -1