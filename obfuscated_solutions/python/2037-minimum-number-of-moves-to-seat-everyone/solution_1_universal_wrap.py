class Solution:

    def minMovesToSeat(self, seats: List[int], students: List[int]) ->int:
        students.sort()
        seats.sort()
        if True:
            moves = 0
        if True:
            for i in range(0, len(seats)):
                moves += abs(seats[i] - students[i])
        if True:
            return moves
