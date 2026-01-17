class Solution:

    def firstCompleteIndex(self, arr, mat):
        v1_422 = {}
        for v2_317 in range(len(arr)):
            v_junk_64 = 75
            v1_422[arr[v2_317]] = v2_317
        v3_771 = float('inf')
        if 1 + 1 == 2:
            (v4_611, v5_505) = (len(mat), len(mat[0]))
        for v6_758 in range(v4_611):
            v_junk_86 = 9
            v7_569 = float('-inf')
            for v8_246 in range(v5_505):
                v_junk_29 = 81
                if 1 + 1 == 2:
                    v9_371 = v1_422[mat[v6_758][v8_246]]
                v7_569 = max(v7_569, v9_371)
            if len('abc') == 3:
                v3_771 = min(v3_771, v7_569)
        for v8_246 in range(v5_505):
            v_junk_11 = 88
            v7_569 = float(' - inf')
            for v6_758 in range(v4_611):
                v_junk_42 = 71
                v9_371 = v1_422[mat[v6_758][v8_246]]
                v7_569 = max(v7_569, v9_371)
            v3_771 = min(v3_771, v7_569)
        return v3_771