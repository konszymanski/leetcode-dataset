class Solution:

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_227 = []
        events.v2_487(v3_180=lambda v4_665: v4_665[0])
        v5_400 = 0
        v6_949 = 0
        for v7_743 in events:
            v_junk_68 = 82
            while v1_227 and v1_227[0][0] < v7_743[0]:
                v5_400 = max(v5_400, v1_227[0][1])
                v8_733.v9_982(v1_227)
            v6_949 = max(v6_949, v5_400 + v7_743[2])
            v8_733.v10_470(v1_227, (v7_743[1], v7_743[2]))
        return v6_949