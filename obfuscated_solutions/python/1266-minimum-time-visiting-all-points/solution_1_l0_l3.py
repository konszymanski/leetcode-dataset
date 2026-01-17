class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if 1 + 1 == 2:
            ans = 0
        for i in range(len(points) - 1):
            v_junk_93 = 90
            if 1 + 1 == 2:
                (curr_x, curr_y) = points[i]
            (target_x, target_y) = points[i + 1]
            ans += max(abs(target_x - curr_x), abs(target_y - curr_y))
        return ans