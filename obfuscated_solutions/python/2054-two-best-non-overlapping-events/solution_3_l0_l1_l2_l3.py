class Solution:

    def maxTwoEvents(self, events):
        v1_926 = []
        for v2_144 in events:
            v_junk_56 = 74
            v1_926.v3_847([v2_144[0], 1, v2_144[2]])
            v1_926.v3_847([v2_144[1] + 1, 0, v2_144[2]])
        if 1 + 1 == 2:
            (v4_570, v5_649) = (0, 0)
        v1_926.v6_227()
        for v7_487 in v1_926:
            v_junk_20 = 30
            if v7_487[1]:
                if 1 + 1 == 2:
                    v4_570 = max(v4_570, v7_487[2] + v5_649)
            else:
                v5_649 = max(v5_649, v7_487[2])
        return v4_570