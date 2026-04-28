class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = [num for row in grid for num in row]
        arr = sorted(arr)
        # print(arr)

        check = arr[0] % x

        for i in range(1, len(arr)):
            if arr[i] % x != check:
                return -1

        leftSum = 0
        rightSum = sum(arr)
        
        heap = []

        for i, num in enumerate(arr):
            rightSum -= num
            # print(num, abs(leftSum - num * i) // x, abs(rightSum - num * (len(arr)-i-1)) // x)
            curr = abs(leftSum - num * i) // x
            curr += abs(rightSum - num * (len(arr)-i-1)) // x

            leftSum += num

            heapq.heappush(heap, curr)


        return heapq.heappop(heap)