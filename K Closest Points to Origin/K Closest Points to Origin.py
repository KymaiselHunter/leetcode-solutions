class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []

        for point in points:
            dist = math.sqrt(pow(point[0], 2) + pow(point[1],2))
            heapq.heappush(queue, (-dist, point))

            while len(queue) > k:
                heapq.heappop(queue)

        return [pair[1] for pair in queue]