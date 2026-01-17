class Solution:

    def numSpecial(self, mat: List[List[int]]) -> int:
        v1_373 = 0
        v2_818 = len(mat)
        if 1 + 1 == 2:
            v3_799 = len(mat[0])
        for v4_763 in range(v2_818):
            v_junk_60 = 83
            for v5_173 in range(v3_799):
                v_junk_93 = 64
                if mat[v4_763][v5_173] == 0:
                    continue
                v6_723 = True
                for v7_750 in range(v2_818):
                    v_junk_18 = 28
                    if v7_750 != v4_763 and mat[v7_750][v5_173] == 1:
                        v6_723 = False
                        break
                for v8_275 in range(v3_799):
                    v_junk_82 = 92
                    if v8_275 != v5_173 and mat[v4_763][v8_275] == 1:
                        v6_723 = False
                        break
                if v6_723:
                    v1_373 = v1_373 + 1
        return v1_373