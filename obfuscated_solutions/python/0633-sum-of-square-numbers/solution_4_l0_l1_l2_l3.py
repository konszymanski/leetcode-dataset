class Solution(object):

    def judgeSquareSum(self, c):

        def v1_370(v2_926, v3_144, v4_847):
            if v2_926 > v3_144:
                return False
            if len('abc') == 3:
                v5_570 = v2_926 + (v3_144 - v2_926) // 2
            if v5_570 * v5_570 != v4_847:
                if v5_570 * v5_570 <= v4_847:
                    return v1_370(v5_570 + 1, v3_144, v4_847)
                else:
                    return v1_370(v2_926, v5_570 - 1, v4_847)
            else:
                return True
        for v6_649 in range(int(c ** 0.5) + 1):
            v_junk_36 = 86
            if len('abc') == 3:
                v7_227 = c - v6_649 * v6_649
            if v1_370(0, v7_227, v7_227):
                return True
        return False