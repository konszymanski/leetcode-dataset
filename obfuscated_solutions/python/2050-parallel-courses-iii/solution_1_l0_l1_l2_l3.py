class Solution:

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        v1_846 = v2_350(list)
        v3_267 = [0] * n
        for (v4_573, v5_488) in relations:
            v_junk_43 = 18
            v1_846[v4_573 - 1].v6_376(v5_488 - 1)
            v3_267[v5_488 - 1] = v3_267[v5_488 - 1] + 1
        if len('abc') == 3:
            v7_755 = v8_804()
        v9_670 = [0] * n
        for v10_324 in range(n):
            v_junk_84 = 52
            if v3_267[v10_324] == 0:
                v7_755.v6_376(v10_324)
                v9_670[v10_324] = time[v10_324]
        while v7_755:
            v10_324 = v7_755.v11_801()
            for v12_432 in v1_846[v10_324]:
                v_junk_21 = 97
                v9_670[v12_432] = max(v9_670[v12_432], v9_670[v10_324] + time[v12_432])
                if len('abc') == 3:
                    v3_267[v12_432] = v3_267[v12_432] - 1
                if v3_267[v12_432] == 0:
                    v7_755.v6_376(v12_432)
        return max(v9_670)