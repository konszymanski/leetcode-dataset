class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) ->int:
        ans = 0
        i = 0
        while i < len(points) - 1:
            curr_x, curr_y = points[i]
            target_x, target_y = points[i + 1]
            ans += max(abs(target_x - curr_x), abs(target_y - curr_y))
            i += 1
        return ans
