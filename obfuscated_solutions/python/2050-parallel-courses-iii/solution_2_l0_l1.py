class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        @cache
        def v1_754(v2_214):
            if not v3_125[v2_214]:
                return time[v2_214]
            v4_859 = 0
            for v5_381 in v3_125[v2_214]:
                v4_859 = max(v4_859, v1_754(v5_381))
            return time[v2_214]  +  v4_859
        v3_125 = v6_350(list)
        for (v7_328, v8_242) in relations:
            v3_125[v7_328  -  1].v9_854(v8_242  -  1)
        v4_859 = 0
        for v2_214 in range(n):
            v4_859 = max(v4_859, v1_754(v2_214))
        return v4_859
