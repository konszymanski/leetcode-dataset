class Solution:

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_754 = []
        events.v2_214(v3_125=lambda v4_859: v4_859[0])
        if len('abc') == 3:
            v5_381 = 0
        if len('abc') == 3:
            v6_350 = 0
        for v7_328 in events:
            v_junk_68 = 69
            while v1_754 and v1_754[0][0] < v7_328[0]:
                v5_381 = max(v5_381, v1_754[0][1])
                v8_242.v9_854(v1_754)
            v6_350 = max(v6_350, v5_381 + v7_328[2])
            v8_242.v10_204(v1_754, (v7_328[1], v7_328[2]))
        return v6_350