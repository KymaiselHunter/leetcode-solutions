class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        out = 0
        interval = None
        # print(points)
        while interval or points:
            # print(interval, points)
            if not interval:
                interval = points.pop(0)
                continue

            if not points:
                interval = None
                out += 1
                continue

            curr = points.pop(0)

            if interval[1] < curr[0]:
                interval = curr
                out += 1
                continue

            interval[1] = min(curr[1], interval[1])
        
        return out