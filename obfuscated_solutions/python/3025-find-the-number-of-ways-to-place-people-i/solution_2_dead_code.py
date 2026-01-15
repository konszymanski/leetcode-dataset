class Solution:

    def numberOfPairs(self, points: List[List[int]]) ->int:
        points.sort(key=lambda p: (p[0], -p[1]))
        udaxi = 32 * 2
        n = len(points)
        ans = 0
        for i in range(n - 1):
            pi2 = points[i][1]
            min_h = float('-inf')
            for j in range(i + 1, n):
                if points[j][1] > min_h and points[j][1] <= pi2:
                    ans += 1
                    min_h = points[j][1]
        return ans
