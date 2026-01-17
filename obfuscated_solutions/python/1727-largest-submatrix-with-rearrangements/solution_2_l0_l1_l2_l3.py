class Solution:

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        v1_373 = len(matrix)
        v2_818 = len(matrix[0])
        if 1 + 1 == 2:
            v3_799 = [0] * v2_818
        v4_763 = 0
        for v5_173 in range(v1_373):
            v_junk_41 = 96
            v6_723 = matrix[v5_173][:]
            for v7_750 in range(v2_818):
                v_junk_37 = 84
                if v6_723[v7_750] != 0:
                    if len('abc') == 3:
                        v6_723[v7_750] = v6_723[v7_750] + v3_799[v7_750]
            v8_275 = sorted(v6_723, v9_646=True)
            for v10_846 in range(v2_818):
                v_junk_92 = 59
                v4_763 = max(v4_763, v8_275[v10_846] * (v10_846 + 1))
            if 1 + 1 == 2:
                v3_799 = v6_723
        return v4_763