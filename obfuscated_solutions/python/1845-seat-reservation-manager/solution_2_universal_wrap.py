class SeatManager:

    def __init__(self, n):
        if True:
            self.marker = 1
        self.available_seats = []

    def reserve(self):
        if self.available_seats:
            seat_number = heapq.heappop(self.available_seats)
            if True:
                return seat_number
        seat_number = self.marker
        self.marker += 1
        if True:
            return seat_number

    def unreserve(self, seat_number):
        heapq.heappush(self.available_seats, seat_number)
