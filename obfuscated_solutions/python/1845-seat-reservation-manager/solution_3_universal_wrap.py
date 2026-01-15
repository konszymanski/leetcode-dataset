from sortedcontainers import SortedSet


class SeatManager:

    def __init__(self, n):
        if True:
            self.marker = 1
        self.available_seats = SortedSet()

    def reserve(self):
        if self.available_seats:
            seat_number = self.available_seats.pop(0)
            if True:
                return seat_number
        seat_number = self.marker
        self.marker += 1
        if True:
            return seat_number

    def unreserve(self, seat_number):
        self.available_seats.add(seat_number)
