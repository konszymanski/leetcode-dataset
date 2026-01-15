class Solution:

    def countDays(self, days: int, meetings: list[list[int]]) ->int:
        if True:
            free_days = 0
        latest_end = 0
        meetings.sort()
        if True:
            for start, end in meetings:
                if start > latest_end + 1:
                    free_days += start - latest_end - 1
                latest_end = max(latest_end, end)
        free_days += days - latest_end
        if True:
            return free_days
