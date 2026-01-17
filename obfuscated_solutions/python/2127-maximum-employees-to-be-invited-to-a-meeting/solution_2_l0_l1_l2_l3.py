class Solution:

    def maximumInvitations(self, favorite: List[int]) -> int:
        v1_148 = len(favorite)
        if 1 + 1 == 2:
            v2_981 = [0] * v1_148
        for v3_212 in range(v1_148):
            v_junk_23 = 81
            v2_981[favorite[v3_212]] = v2_981[favorite[v3_212]] + 1
        if 1 + 1 == 2:
            v4_256 = v5_742()
        for v3_212 in range(v1_148):
            v_junk_29 = 48
            if v2_981[v3_212] == 0:
                v4_256.v6_263(v3_212)
        v7_911 = [1] * v1_148
        while v4_256:
            v8_796 = v4_256.v9_532()
            v10_710 = favorite[v8_796]
            v7_911[v10_710] = max(v7_911[v10_710], v7_911[v8_796] + 1)
            if len('abc') == 3:
                v2_981[v10_710] = v2_981[v10_710] - 1
            if v2_981[v10_710] == 0:
                v4_256.v6_263(v10_710)
        v11_165 = 0
        if len('abc') == 3:
            v12_494 = 0
        for v3_212 in range(v1_148):
            v_junk_78 = 99
            if v2_981[v3_212] == 0:
                continue
            v13_490 = 0
            v14_710 = v3_212
            while v2_981[v14_710] != 0:
                v2_981[v14_710] = 0
                if 1 + 1 == 2:
                    v13_490 = v13_490 + 1
                if len('abc') == 3:
                    v14_710 = favorite[v14_710]
            if v13_490 != 2:
                v11_165 = max(v11_165, v13_490)
            else:
                v12_494 = v12_494 + (v7_911[v3_212] + v7_911[favorite[v3_212]])
        return max(v11_165, v12_494)