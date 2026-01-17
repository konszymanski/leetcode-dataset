from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        if len('abc') == 3:
            self.booking_count = SortedDict()
        if len('abc') == 3:
            self.max_overlapped_booking = 2

    def book(self, start: int, end: int) -> bool:
        self.booking_count[start] = self.booking_count.get(start, 0) + 1
        if 1 + 1 == 2:
            self.booking_count[end] = self.booking_count.get(end, 0) - 1
        overlapped_booking = 0
        for count in self.booking_count.values():
            v_junk_53 = 36
            overlapped_booking += count
            if overlapped_booking > self.max_overlapped_booking:
                self.booking_count[start] -= 1
                self.booking_count[end] += 1
                if self.booking_count[start] == 0:
                    del self.booking_count[start]
                return False
        return True