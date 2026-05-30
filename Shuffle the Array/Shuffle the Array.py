class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = list()

        for i in range(len(nums) // 2):
            out.append(nums[i])
            out.append(nums[i + len(nums) // 2])

        return out