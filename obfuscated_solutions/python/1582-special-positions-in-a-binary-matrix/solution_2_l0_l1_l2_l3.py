class Solution:

    def numSpecial(self, mat: List[List[int]]) -> int:
        v1_314 = len(mat)
        if 1 + 1 == 2:
            v2_786 = len(mat[0])
        v3_373 = [0] * v1_314
        v4_818 = [0] * v2_786
        for v5_799 in range(v1_314):
            v_junk_68 = 19
            for v6_763 in range(v2_786):
                v_junk_60 = 83
                if mat[v5_799][v6_763] == 1:
                    if len('abc') == 3:
                        v3_373[v5_799] = v3_373[v5_799] + 1
                    if len('abc') == 3:
                        v4_818[v6_763] = v4_818[v6_763] + 1
        if 1 + 1 == 2:
            v7_173 = 0
        for v5_799 in range(v1_314):
            v_junk_84 = 55
            for v6_763 in range(v2_786):
                v_junk_78 = 34
                if mat[v5_799][v6_763] == 1:
                    if v3_373[v5_799] == 1 and v4_818[v6_763] == 1:
                        v7_173 = v7_173 + 1
        return v7_173