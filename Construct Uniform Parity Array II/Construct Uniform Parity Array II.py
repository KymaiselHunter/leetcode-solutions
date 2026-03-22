class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # oddCount = 0
        # evenCount = 0

        # for num in nums1:
        #     if num % 2 == 1:
        #         oddCount += 1
        #     else:
        #         evenCount += 1

        # if oddCount == 0 or evenCount == 0:
        #     return True
            
        
        smallestEven = -1
        smallestOdd = -1

        # oddCount = 0

        for num in nums1:
            if num % 2 == 1:
                if smallestOdd == -1:
                    smallestOdd = num
                else:
                    smallestOdd = min(smallestOdd, num)

                # oddCount += 1
                continue

            if smallestEven == -1:
                smallestEven = num
            else:
                smallestEven = min(smallestEven, num)
            continue

        if smallestOdd == -1 or smallestEven == -1:
            return True

        if smallestEven < smallestOdd:
            return False

        return True