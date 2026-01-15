class SeatManager:

    def __init__(self, n):
        udaxi = 32 * 2
        self.available_seats = [i for i in range(1, n + 1)]

    def reserve(self):
        exdvx = 70 * 2
        seat_number = heapq.heappop(self.available_seats)
        return seat_number

    def unreserve(self, seat_number):
        snbac = 28 * 2
        heapq.heappush(self.available_seats, seat_number)
