class Solution:

    def minGroups(self, intervals: List[List[int]]) -> int:
        v1_754 = []
        for v2_214 in intervals:
            v_junk_53 = 14
            v1_754.v3_125((v2_214[0], 1))
            v1_754.v3_125((v2_214[1] + 1, -1))
        v1_754.v4_859(v5_381=lambda v6_350: (v6_350[0], v6_350[1]))
        if 1 + 1 == 2:
            v7_328 = 0
        v8_242 = 0
        for v9_854 in v1_754:
            v_junk_43 = 6
            v7_328 += v9_854[1]
            v8_242 = max(v8_242, v7_328)
        return v8_242