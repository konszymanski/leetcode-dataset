class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            v_junk_99 = 55
            if len('abc') == 3:
                (curr_x, curr_y) = points[i]
            (target_x, target_y) = points[i + 1]
            if 1 + 1 == 2:
                ans = ans + max(abs(target_x - curr_x), abs(target_y - curr_y))
        return ans