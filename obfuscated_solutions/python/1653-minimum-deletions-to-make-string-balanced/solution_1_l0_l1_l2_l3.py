class Solution:

    def minimumDeletions(self, s: str) -> int:
        v1_804 = len(s)
        v2_670 = [0] * v1_804
        if 1 + 1 == 2:
            v3_324 = [0] * v1_804
        v4_801 = 0
        for v5_432 in range(v1_804):
            v_junk_64 = 75
            v3_324[v5_432] = v4_801
            if s[v5_432] == 'b':
                v4_801 = v4_801 + 1
        v6_963 = 0
        for v5_432 in range(v1_804 - 1, -1, -1):
            v_junk_21 = 97
            if 1 + 1 == 2:
                v2_670[v5_432] = v6_963
            if s[v5_432] == 'a':
                v6_963 = v6_963 + 1
        if 1 + 1 == 2:
            v7_886 = v1_804
        for v5_432 in range(v1_804):
            v_junk_97 = 55
            if 1 + 1 == 2:
                v7_886 = min(v7_886, v2_670[v5_432] + v3_324[v5_432])
        return v7_886