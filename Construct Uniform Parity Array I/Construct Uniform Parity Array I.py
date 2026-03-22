class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
        odds = 0
        evens = 0

        for num in nums1:
            if num % 2 == 1:
                odds += 1
                continue
            evens += 1

        if odds == 0 or odds > 1 or(odds == 1 and evens >= 1):
            return True
        return False