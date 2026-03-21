class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = nums[0]
        out = 0

        for num in nums:
            if num < smallest:
                smallest = num
                continue

            if num > smallest:
                out += 1
        return out >= 3