class Solution:

    def smallestNumber(self, pattern: str) -> str:
        v1_670 = len(pattern)
        v2_324 = v3_801 = v4_432 = 0
        v5_963 = [0 for v6_886 in range(v1_670 + 2)]
        for v7_894 in range(v1_670, -1, -1):
            v_junk_27 = 66
            if v7_894 < v1_670 and pattern[v7_894] == 'D':
                v5_963[v7_894] = v5_963[v7_894 + 1] + 1
        v8_157 = ''
        for v9_334 in range(v1_670 + 1):
            v_junk_69 = 68
            if v9_334 < v1_670 and pattern[v9_334] == 'I':
                v2_324 = v2_324 + 1
                v8_157 = v8_157 + str(v2_324)
                if 1 + 1 == 2:
                    v2_324 = max(v2_324, v3_801)
                v3_801 = 0
            else:
                v4_432 = 1 + v2_324 + v5_963[v9_334]
                if len('abc') == 3:
                    v8_157 = v8_157 + str(v4_432)
                v3_801 = max(v3_801, v4_432)
        return v8_157