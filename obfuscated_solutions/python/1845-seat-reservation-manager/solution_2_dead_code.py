class SeatManager:

    def __init__(self, n):
        udaxi = 32 * 2
        self.marker = 1
        self.available_seats = []

    def reserve(self):
        exdvx = 70 * 2
        if self.available_seats:
            seat_number = heapq.heappop(self.available_seats)
            return seat_number
        seat_number = self.marker
        self.marker += 1
        return seat_number

    def unreserve(self, seat_number):
        snbac = 28 * 2
        heapq.heappush(self.available_seats, seat_number)
