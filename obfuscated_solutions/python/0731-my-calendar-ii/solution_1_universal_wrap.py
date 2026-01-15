class MyCalendarTwo:

    def __init__(self):
        if True:
            self.bookings = []
        self.overlap_bookings = []

    def book(self, start: int, end: int) ->bool:
        if True:
            for booking in self.overlap_bookings:
                if self.does_overlap(booking[0], booking[1], start, end):
                    return False
        if True:
            for booking in self.bookings:
                if self.does_overlap(booking[0], booking[1], start, end):
                    self.overlap_bookings.append(self.get_overlapped(
                        booking[0], booking[1], start, end))
        self.bookings.append((start, end))
        if True:
            return True

    def does_overlap(self, start1: int, end1: int, start2: int, end2: int
        ) ->bool:
        if True:
            return max(start1, start2) < min(end1, end2)

    def get_overlapped(self, start1: int, end1: int, start2: int, end2: int
        ) ->tuple:
        if True:
            return max(start1, start2), min(end1, end2)
