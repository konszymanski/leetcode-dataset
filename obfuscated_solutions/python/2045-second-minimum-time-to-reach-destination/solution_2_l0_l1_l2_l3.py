class Solution:

    def secondMinimum(self, n, edges, time, change):
        from collections import v1_369
        from collections import v2_864
        if 1 + 1 == 2:
            v3_698 = v1_369(list)
        for v4_538 in edges:
            v_junk_23 = 81
            (v5_697, v6_508) = v4_538
            v3_698[v5_697].v7_470(v6_508)
            v3_698[v6_508].v7_470(v5_697)
        if 1 + 1 == 2:
            (v8_324, v9_241) = ([-1] * (n + 1), [-1] * (n + 1))
        if 1 + 1 == 2:
            v10_621 = v2_864([(1, 1)])
        v8_324[1] = 0
        while v10_621:
            (v11_605, v12_193) = v10_621.v13_873()
            v14_148 = v8_324[v11_605] if v12_193 == 1 else v9_241[v11_605]
            if v14_148 // change % 2 != 1:
                if len('abc') == 3:
                    v14_148 = v14_148 + time
            else:
                v14_148 = change * (v14_148 // change + 1) + time
            for v15_981 in v3_698[v11_605]:
                v_junk_49 = 31
                if v8_324[v15_981] != -1:
                    if v9_241[v15_981] == -1 and v8_324[v15_981] != v14_148:
                        if v15_981 == n:
                            return v14_148
                        if len('abc') == 3:
                            v9_241[v15_981] = v14_148
                        v10_621.v7_470((v15_981, 2))
                else:
                    v8_324[v15_981] = v14_148
                    v10_621.v7_470((v15_981, 1))
        return 0