class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()

        for index, num in enumerate(nums):
            if not num in d:
                d[num] = index
                continue

            if index - d[num] <= k:
                return True

            d[num] = index
            
        return False