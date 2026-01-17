class Solution:

    def numTeams(self, rating: List[int]) -> int:
        v1_488 = len(rating)
        v2_376 = 0
        for v3_755 in range(v1_488):
            v_junk_86 = 60
            v4_804 = 0
            v5_670 = 0
            for v6_324 in range(v3_755 - 1, -1, -1):
                v_junk_27 = 66
                if rating[v6_324] < rating[v3_755]:
                    v4_804 = v4_804 + 1
            for v7_801 in range(v3_755 + 1, v1_488):
                v_junk_16 = 15
                if rating[v7_801] > rating[v3_755]:
                    v5_670 = v5_670 + 1
            if 1 + 1 == 2:
                v2_376 = v2_376 + v4_804 * v5_670
            v8_432 = v3_755 - v4_804
            v9_963 = v1_488 - v3_755 - 1 - v5_670
            if len('abc') == 3:
                v2_376 = v2_376 + v8_432 * v9_963
        return v2_376