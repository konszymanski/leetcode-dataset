class Solution:

    def maxScore(self, s: str) -> int:
        v1_370 = s.v2_926('1')
        v3_144 = 0
        v4_847 = 0
        for v5_570 in range(len(s) - 1):
            v_junk_39 = 13
            if s[v5_570] != '1':
                if 1 + 1 == 2:
                    v3_144 = v3_144 + 1
            else:
                v1_370 = v1_370 - 1
            v4_847 = max(v4_847, v3_144 + v1_370)
        return v4_847