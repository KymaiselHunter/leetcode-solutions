class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = float('inf')
        smallest = float('inf')

        for num in nums:
            if num < small:
                small = num
            elif num < smallest:
                smallest = num
            else:
                return True

        return False

