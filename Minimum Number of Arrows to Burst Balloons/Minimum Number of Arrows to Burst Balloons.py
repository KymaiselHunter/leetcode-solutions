class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        out = 0
        interval = None
        it = 0
        # print(points)
        while interval or it < len(points):
            # print(interval, points)
            if not interval:
                interval = points[it]
                it += 1
                continue

            if it >= len(points):
                interval = None
                out += 1
                continue

            curr = points[it]
            it += 1

            if interval[1] < curr[0]:
                interval = curr
                out += 1
                continue

            interval[1] = min(curr[1], interval[1])
        
        return out