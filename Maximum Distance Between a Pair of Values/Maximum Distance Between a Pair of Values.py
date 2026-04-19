class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        left = len(nums1)-1
        right = len(nums2)-1
        out = 0

        while left >= 0 and right >= 0:

            while left >= 0 and nums1[left] <= nums2[right]:
                out = max(out, right - left)
                left -= 1

            right -= 1

        return out