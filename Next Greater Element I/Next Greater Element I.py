class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = defaultdict(lambda: -1)
        stack = list()
        
        for num in nums2:
            while stack and stack[-1] < num:
                mp[stack.pop()] = num
            
            stack.append(num)

        return [mp[num] for num in nums1]
