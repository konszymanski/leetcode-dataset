class Solution:

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        v1_754 = [0] * (len(travel) + 1)
        v1_754[1] = travel[0]
        for v2_214 in range(1, len(travel)):
            v1_754[v2_214 + 1] = v1_754[v2_214] + travel[v2_214]
        v3_125 = {}
        v4_859 = {}
        for v2_214 in range(len(garbage)):
            for v5_381 in garbage[v2_214]:
                v3_125[v5_381] = v2_214
                v4_859[v5_381] = v4_859.v6_350(v5_381, 0) + 1
        v7_328 = 'MPG'
        v8_242 = 0
        for v5_381 in v7_328:
            if v5_381 in v4_859:
                v8_242 = v8_242 + (v1_754[v3_125[v5_381]] + v4_859[v5_381])
        return v8_242