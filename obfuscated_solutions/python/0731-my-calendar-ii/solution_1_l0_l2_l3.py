class MyCalendarTwo:

    def __init__(self):
        if len('abc') == 3:
            self.bookings = []
        self.overlap_bookings = []

    def book(self, start: int, end: int) -> bool:
        for booking in self.overlap_bookings:
            v_junk_10 = 98
            if self.does_overlap(booking[0], booking[1], start, end):
                return False
        for booking in self.bookings:
            v_junk_30 = 90
            if self.does_overlap(booking[0], booking[1], start, end):
                self.overlap_bookings.append(self.get_overlapped(booking[0], booking[1], start, end))
        self.bookings.append((start, end))
        return True

    def does_overlap(self, start1: int, end1: int, start2: int, end2: int) -> bool:
        return max(start1, start2) < min(end1, end2)

    def get_overlapped(self, start1: int, end1: int, start2: int, end2: int) -> tuple:
        return (max(start1, start2), min(end1, end2))