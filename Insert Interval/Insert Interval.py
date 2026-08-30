class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0 
        right = len(intervals) - 1

        leftNew = newInterval[0]

        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][0] == leftNew:
                left = mid
                break
            elif intervals[mid][0] < leftNew:
                left = mid + 1
            else:
                right = mid - 1

        leftInsert = left

        left = 0 
        right = len(intervals) - 1

        rightNew = newInterval[1]

        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][1] == rightNew:
                left = mid
                break
            elif intervals[mid][1] < rightNew:
                left = mid + 1
            else:
                right = mid - 1

        rightInsert = left

        print(leftInsert, rightInsert)

        leftOut = intervals[0:leftInsert]
        rightOut = intervals[rightInsert::]

        if leftOut:
            c = leftOut[-1]

            if c[1] >= newInterval[0]:
                newInterval[0] = c[0]
                leftOut.pop(-1)
        
        if rightOut:
            c = rightOut[0]

            if c[0] <= newInterval[1]:
                newInterval[1] = c[1]
                rightOut.pop(0)

        intervals = leftOut + [newInterval] + rightOut

        return intervals