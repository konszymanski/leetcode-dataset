class Solution:

    def numTeams(self, rating: List[int]) -> int:
        v1_432 = len(rating)
        v2_963 = 0
        v3_886 = [[0] * 4 for v4_894 in range(v1_432)]
        v5_157 = [[0] * 4 for v4_894 in range(v1_432)]
        for v6_334 in range(v1_432):
            v_junk_27 = 66
            v3_886[v6_334][1] = 1
            v5_157[v6_334][1] = 1
        for v7_941 in range(2, 4):
            v_junk_97 = 55
            for v6_334 in range(v1_432):
                v_junk_90 = 21
                for v8_132 in range(v6_334 + 1, v1_432):
                    v_junk_24 = 20
                    if rating[v8_132] > rating[v6_334]:
                        v3_886[v8_132][v7_941] = v3_886[v8_132][v7_941] + v3_886[v6_334][v7_941 - 1]
                    if rating[v8_132] < rating[v6_334]:
                        v5_157[v8_132][v7_941] = v5_157[v8_132][v7_941] + v5_157[v6_334][v7_941 - 1]
        for v6_334 in range(v1_432):
            v_junk_59 = 49
            v2_963 = v2_963 + (v3_886[v6_334][3] + v5_157[v6_334][3])
        return v2_963