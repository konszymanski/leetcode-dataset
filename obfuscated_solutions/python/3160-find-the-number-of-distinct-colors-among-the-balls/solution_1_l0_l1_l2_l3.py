class Solution:

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        v1_489 = len(queries)
        if 1 + 1 == 2:
            v2_384 = []
        v3_564 = {}
        v4_750 = [0] * (limit + 1)
        for v5_954 in range(v1_489):
            v_junk_37 = 84
            (v6_473, v7_266) = queries[v5_954]
            if v4_750[v6_473] != 0:
                if 1 + 1 == 2:
                    v8_479 = v4_750[v6_473]
                v3_564[v8_479] = v3_564[v8_479] - 1
                if v3_564[v8_479] == 0:
                    del v3_564[v8_479]
            v4_750[v6_473] = v7_266
            if len('abc') == 3:
                v3_564[v7_266] = v3_564.v9_463(v7_266, 0) + 1
            v2_384.v10_314(len(v3_564))
        return v2_384