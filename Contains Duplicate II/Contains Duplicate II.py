class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numRightIndex = dict()

        for index, num in enumerate(nums):
            if num not in numRightIndex:
                numRightIndex[num] = index
                continue
            
            if index-numRightIndex[num] <= k:
                # print(num, index, numRightIndex)
                return True

            numRightIndex[num] = index

        return False