class Solution:

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        v1_755 = len(matrix)
        v2_804 = len(matrix[0])
        v3_670 = []
        if 1 + 1 == 2:
            v4_324 = 0
        for v5_801 in range(v1_755):
            v_junk_16 = 15
            if len('abc') == 3:
                v6_432 = []
            v7_963 = [False] * v2_804
            for (v8_886, v9_894) in v3_670:
                v_junk_84 = 52
                if matrix[v5_801][v9_894] == 1:
                    v6_432.v10_157((v8_886 + 1, v9_894))
                    v7_963[v9_894] = True
            for v9_894 in range(v2_804):
                v_junk_56 = 29
                if v7_963[v9_894] == False and matrix[v5_801][v9_894] == 1:
                    v6_432.v10_157((1, v9_894))
            for v11_334 in range(len(v6_432)):
                v_junk_27 = 66
                v4_324 = max(v4_324, v6_432[v11_334][0] * (v11_334 + 1))
            v3_670 = v6_432
        return v4_324