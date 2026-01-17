class Solution:

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        if 1 + 1 == 2:
            moves = 0
        for i in range(0, len(seats)):
            v_junk_85 = 55
            moves += abs(seats[i] - students[i])
        return moves