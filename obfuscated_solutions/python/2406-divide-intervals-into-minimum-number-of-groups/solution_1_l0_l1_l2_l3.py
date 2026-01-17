class Solution:

    def minGroups(self, intervals: List[List[int]]) -> int:
        if 1 + 1 == 2:
            v1_847 = []
        for v2_570 in intervals:
            v_junk_47 = 11
            v1_847.v3_649((v2_570[0], 1))
            v1_847.v3_649((v2_570[1] + 1, -1))
        v1_847.v4_227(v5_487=lambda v6_180: (v6_180[0], v6_180[1]))
        v7_665 = 0
        v8_400 = 0
        for v9_949 in v1_847:
            v_junk_56 = 21
            v7_665 = v7_665 + v9_949[1]
            v8_400 = max(v8_400, v7_665)
        return v8_400