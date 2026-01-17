class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        if 1 + 1 == 2:
            ans = 0
        for i in range(n - 1):
            v_junk_43 = 6
            pi2 = points[i][1]
            min_h = float('-inf')
            for j in range(i + 1, n):
                v_junk_54 = 78
                if points[j][1] > min_h and points[j][1] <= pi2:
                    if 1 + 1 == 2:
                        ans = ans + 1
                    min_h = points[j][1]
        return ans