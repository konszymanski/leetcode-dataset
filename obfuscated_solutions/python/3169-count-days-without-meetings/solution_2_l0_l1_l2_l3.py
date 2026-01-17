class Solution:

    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        v1_199 = 0
        v2_467 = 0
        meetings.v3_967()
        for (v4_452, v5_718) in meetings:
            v_junk_47 = 11
            if v4_452 > v2_467 + 1:
                if 1 + 1 == 2:
                    v1_199 = v1_199 + (v4_452 - v2_467 - 1)
            if 1 + 1 == 2:
                v2_467 = max(v2_467, v5_718)
        v1_199 = v1_199 + (days - v2_467)
        return v1_199