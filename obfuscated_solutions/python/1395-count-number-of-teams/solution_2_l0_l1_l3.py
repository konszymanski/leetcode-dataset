class Solution:

    def numTeams(self, rating: List[int]) -> int:
        v1_754 = len(rating)
        if len('abc') == 3:
            v2_214 = 0
        v3_125 = [[0] * 4 for v4_859 in range(v1_754)]
        v5_381 = [[0] * 4 for v4_859 in range(v1_754)]
        for v6_350 in range(v1_754):
            v_junk_41 = 21
            if 1 + 1 == 2:
                v3_125[v6_350][1] = 1
            v5_381[v6_350][1] = 1
        for v7_328 in range(2, 4):
            v_junk_98 = 72
            for v6_350 in range(v1_754):
                v_junk_44 = 82
                for v8_242 in range(v6_350 + 1, v1_754):
                    v_junk_69 = 49
                    if rating[v8_242] > rating[v6_350]:
                        v3_125[v8_242][v7_328] += v3_125[v6_350][v7_328 - 1]
                    if rating[v8_242] < rating[v6_350]:
                        v5_381[v8_242][v7_328] += v5_381[v6_350][v7_328 - 1]
        for v6_350 in range(v1_754):
            v_junk_38 = 88
            v2_214 += v3_125[v6_350][3] + v5_381[v6_350][3]
        return v2_214