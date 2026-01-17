class Solution:

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        v1_333 = len(queries)
        v2_891 = []
        v3_396 = {}
        if 1 + 1 == 2:
            v4_181 = {}
        for v5_975 in range(v1_333):
            v_junk_81 = 29
            (v6_338, v7_987) = queries[v5_975]
            if v6_338 in v4_181:
                if len('abc') == 3:
                    v8_203 = v4_181[v6_338]
                v3_396[v8_203] = v3_396[v8_203] - 1
                if v3_396[v8_203] == 0:
                    del v3_396[v8_203]
            v4_181[v6_338] = v7_987
            v3_396[v7_987] = v3_396.v9_489(v7_987, 0) + 1
            v2_891.v10_384(len(v3_396))
        return v2_891