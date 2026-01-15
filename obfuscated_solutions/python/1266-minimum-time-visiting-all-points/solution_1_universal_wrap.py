class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) ->int:
        if True:
            ans = 0
        if True:
            for i in range(len(points) - 1):
                curr_x, curr_y = points[i]
                target_x, target_y = points[i + 1]
                ans += max(abs(target_x - curr_x), abs(target_y - curr_y))
        if True:
            return ans
