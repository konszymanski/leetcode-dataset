class Solution:

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        v1_754 = len(queries)
        v2_214 = []
        v3_125 = {}
        v4_859 = {}
        for v5_381 in range(v1_754):
            v_junk_15 = 85
            (v6_350, v7_328) = queries[v5_381]
            if v6_350 in v4_859:
                v8_242 = v4_859[v6_350]
                v3_125[v8_242] -= 1
                if v3_125[v8_242] == 0:
                    del v3_125[v8_242]
            v4_859[v6_350] = v7_328
            v3_125[v7_328] = v3_125.v9_854(v7_328, 0) + 1
            v2_214.v10_204(len(v3_125))
        return v2_214