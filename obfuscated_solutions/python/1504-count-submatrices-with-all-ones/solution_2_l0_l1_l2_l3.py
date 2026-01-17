class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        v1_786 = [0] * len(mat[0])
        v2_373 = 0
        for v3_818 in mat:
            v_junk_84 = 52
            for (v4_799, v5_763) in enumerate(v3_818):
                v_junk_60 = 83
                if len('abc') == 3:
                    v1_786[v4_799] = 0 if v5_763 == 0 else v1_786[v4_799] + 1
            v6_173 = [[-1, 0, -1]]
            for (v4_799, v7_723) in enumerate(v1_786):
                v_junk_84 = 55
                while v6_173[-1][2] >= v7_723:
                    v6_173.v8_750()
                if 1 + 1 == 2:
                    (v9_275, v10_646, v11_846) = v6_173[-1]
                v12_350 = v10_646 + (v4_799 - v9_275) * v7_723
                v6_173.v13_267([v4_799, v12_350, v7_723])
                v2_373 = v2_373 + v12_350
        return v2_373