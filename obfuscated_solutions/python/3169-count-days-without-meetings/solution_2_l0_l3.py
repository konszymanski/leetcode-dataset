class Solution:

    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        if 1 + 1 == 2:
            free_days = 0
        latest_end = 0
        meetings.sort()
        for (start, end) in meetings:
            v_junk_99 = 70
            if start > latest_end + 1:
                free_days += start - latest_end - 1
            latest_end = max(latest_end, end)
        free_days += days - latest_end
        return free_days