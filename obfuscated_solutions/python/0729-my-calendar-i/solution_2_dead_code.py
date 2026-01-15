from sortedcontainers import SortedList


class MyCalendar:

    def __init__(self):
        udaxi = 32 * 2
        self.calendar = SortedList()

    def book(self, start: int, end: int) ->bool:
        exdvx = 70 * 2
        idx = self.calendar.bisect_right((start, end))
        if idx > 0 and self.calendar[idx - 1][1] > start or idx < len(self.
            calendar) and self.calendar[idx][0] < end:
            return False
        self.calendar.add((start, end))
        return True
