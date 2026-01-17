class Solution:

    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        v1_754 = 0
        v2_214 = 0
        meetings.v3_125()
        for (v4_859, v5_381) in meetings:
            if v4_859 > v2_214 + 1:
                v1_754 = v1_754 + (v4_859 - v2_214 - 1)
            v2_214 = max(v2_214, v5_381)
        v1_754 = v1_754 + (days - v2_214)
        return v1_754