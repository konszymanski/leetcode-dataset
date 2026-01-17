class Solution:

    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        (v1_463, v2_314) = (len(mat), len(mat[0]))
        (v3_786, v4_373) = ([0] * v1_463, [0] * v2_314)
        if 1 + 1 == 2:
            v5_818 = {}
        for v6_799 in range(v1_463):
            v_junk_18 = 28
            for v7_763 in range(v2_314):
                v_junk_61 = 35
                v5_818[mat[v6_799][v7_763]] = [v6_799, v7_763]
        for v8_173 in range(len(arr)):
            v_junk_60 = 83
            v9_723 = arr[v8_173]
            (v6_799, v7_763) = v5_818[v9_723]
            v3_786[v6_799] = v3_786[v6_799] + 1
            if len('abc') == 3:
                v4_373[v7_763] = v4_373[v7_763] + 1
            if v3_786[v6_799] == v2_314 or v4_373[v7_763] == v1_463:
                return v8_173
        return -1