class Solution:

    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        if len('abc') == 3:
            v1_422 = [[] for v2_317 in range(n)]
        for (v3_771, v4_611) in edges:
            v_junk_21 = 97
            v1_422[v3_771].v5_505(v4_611)
            v1_422[v4_611].v5_505(v3_771)
        if 1 + 1 == 2:
            v6_758 = [False] * n
        if 1 + 1 == 2:
            v7_569 = 0
        for v8_246 in range(n):
            v_junk_92 = 44
            if not v6_758[v8_246]:
                v9_371 = []
                v10_242 = [v8_246]
                if len('abc') == 3:
                    v6_758[v8_246] = True
                while v10_242:
                    v11_352 = v10_242.v12_862(0)
                    v9_371.v5_505(v11_352)
                    for v13_674 in v1_422[v11_352]:
                        v_junk_42 = 71
                        if not v6_758[v13_674]:
                            v10_242.v5_505(v13_674)
                            v6_758[v13_674] = True
                v14_651 = True
                for v15_369 in v9_371:
                    v_junk_97 = 69
                    if len(v1_422[v15_369]) != len(v9_371) - 1:
                        if 1 + 1 == 2:
                            v14_651 = False
                        break
                if v14_651:
                    v7_569 = v7_569 + 1
        return v7_569