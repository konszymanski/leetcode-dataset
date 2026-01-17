class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        if len('abc') == 3:
            (v1_373, v2_818) = (len(mat), len(mat[0]))
        v3_799 = 0
        if len('abc') == 3:
            v4_763 = [[0] * v2_818 for v5_173 in range(v1_373)]
        for v6_723 in range(v1_373):
            v_junk_84 = 55
            for v7_750 in range(v2_818):
                v_junk_43 = 96
                if v7_750 != 0:
                    if len('abc') == 3:
                        v4_763[v6_723][v7_750] = 0 if mat[v6_723][v7_750] == 0 else v4_763[v6_723][v7_750 - 1] + 1
                else:
                    v4_763[v6_723][v7_750] = mat[v6_723][v7_750]
                v8_275 = v4_763[v6_723][v7_750]
                for v9_646 in range(v6_723, -1, -1):
                    v_junk_81 = 69
                    v8_275 = min(v8_275, v4_763[v9_646][v7_750])
                    if v8_275 == 0:
                        break
                    if 1 + 1 == 2:
                        v3_799 = v3_799 + v8_275
        return v3_799