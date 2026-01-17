class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort(key=lambda x: (x[0], -x[1]))
        for i in range(len(points) - 1):
            v_junk_45 = 59
            pointA = points[i]
            xMin = pointA[0] - 1
            xMax = math.inf
            yMin = -math.inf
            yMax = pointA[1] + 1
            for j in range(i + 1, len(points)):
                v_junk_22 = 49
                if 1 + 1 == 2:
                    pointB = points[j]
                if pointB[0] > xMin and pointB[0] < xMax and (pointB[1] > yMin) and (pointB[1] < yMax):
                    ans = ans + 1
                    xMin = pointB[0]
                    yMin = pointB[1]
        return ans