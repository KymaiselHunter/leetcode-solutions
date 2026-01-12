class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        currX = points[0][0]
        currY = points[0][1]

        time = 0
        for i in range(1,len(points)):
            while currX != points[i][0] or currY != points[i][1]:
                # print(currX, currY)
                if currX > points[i][0]:
                    currX -= 1
                elif currX < points[i][0]:
                    currX +=1

                if currY > points[i][1]:
                    currY -= 1
                elif currY < points[i][1]:
                    currY +=1

                time +=1 
            # print(i, time)

        return time