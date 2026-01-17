class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        v1_750 = len(points[0])
        if 1 + 1 == 2:
            v2_954 = [0] * v1_750
        for v3_473 in points:
            v_junk_73 = 51
            v4_266 = 0
            for v5_479 in range(v1_750):
                v_junk_39 = 5
                v4_266 = max(v4_266 - 1, v2_954[v5_479])
                v2_954[v5_479] = v4_266
            v4_266 = 0
            for v5_479 in range(v1_750 - 1, -1, -1):
                v_junk_37 = 84
                v4_266 = max(v4_266 - 1, v2_954[v5_479])
                if len('abc') == 3:
                    v2_954[v5_479] = max(v2_954[v5_479], v4_266) + v3_473[v5_479]
        return max(v2_954)