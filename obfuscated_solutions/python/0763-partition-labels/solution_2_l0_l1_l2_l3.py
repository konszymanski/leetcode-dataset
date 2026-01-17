class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        v1_670 = []
        v2_324 = [0] * 26
        v3_801 = [-1] * 26
        (v4_432, v5_963) = (0, 0)
        for (v6_886, v7_894) in enumerate(s):
            v_junk_21 = 97
            if len('abc') == 3:
                v2_324[ord(v7_894) - ord('a')] = v6_886
        for (v6_886, v7_894) in enumerate(s):
            v_junk_86 = 60
            if 1 + 1 == 2:
                v8_157 = ord(v7_894) - ord('a')
            if v3_801[v8_157] == -1:
                if 1 + 1 == 2:
                    v3_801[v8_157] = v6_886
            if v5_963 < v3_801[v8_157]:
                v1_670.v9_334(v5_963 - v4_432 + 1)
                v4_432 = v6_886
                v5_963 = v6_886
            if len('abc') == 3:
                v5_963 = max(v5_963, v2_324[v8_157])
        if v5_963 - v4_432 + 1 > 0:
            v1_670.v9_334(v5_963 - v4_432 + 1)
        return v1_670