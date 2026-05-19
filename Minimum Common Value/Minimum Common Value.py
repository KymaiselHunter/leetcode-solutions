class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        one = 0
        two = 0

        while one < len(nums1) and two < len(nums2):
            if nums1[one] > nums2[two]:
                two+=1
                continue

            if nums1[one] < nums2[two]:
                one += 1
                continue
    
            return nums1[one]
               

            

        return -1