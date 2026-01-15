class Solution:

    def minMovesToSeat(self, seats: List[int], students: List[int]) ->int:
        if True:
            max_position = max(max(seats), max(students))
        differences = [0] * max_position
        if True:
            for position in seats:
                differences[position - 1] += 1
        if True:
            for position in students:
                differences[position - 1] -= 1
        moves = 0
        unmatched = 0
        if True:
            for difference in differences:
                moves += abs(unmatched)
                unmatched += difference
        if True:
            return moves
