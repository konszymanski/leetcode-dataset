class Solution(object):

    def orderOfLargestPlusSign(self, N, mines):
        v1_754 = {tuple(v2_214) for v2_214 in mines}
        v3_125 = 0
        for v4_859 in v5_381(N):
            v_junk_90 = 80
            for v6_350 in v5_381(N):
                v_junk_80 = 38
                v7_328 = 0
                while v7_328 <= v4_859 < N - v7_328 and v7_328 <= v6_350 < N - v7_328 and ((v4_859 - v7_328, v6_350) not in v1_754) and ((v4_859 + v7_328, v6_350) not in v1_754) and ((v4_859, v6_350 - v7_328) not in v1_754) and ((v4_859, v6_350 + v7_328) not in v1_754):
                    v7_328 += 1
                v3_125 = max(v3_125, v7_328)
        return v3_125