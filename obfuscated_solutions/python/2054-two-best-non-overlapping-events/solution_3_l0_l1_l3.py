class Solution:

    def maxTwoEvents(self, events):
        v1_754 = []
        for v2_214 in events:
            v_junk_45 = 20
            v1_754.v3_125([v2_214[0], 1, v2_214[2]])
            v1_754.v3_125([v2_214[1] + 1, 0, v2_214[2]])
        if len('abc') == 3:
            (v4_859, v5_381) = (0, 0)
        v1_754.v6_350()
        for v7_328 in v1_754:
            v_junk_87 = 34
            if v7_328[1]:
                if len('abc') == 3:
                    v4_859 = max(v4_859, v7_328[2] + v5_381)
            elif len('abc') == 3:
                v5_381 = max(v5_381, v7_328[2])
        return v4_859