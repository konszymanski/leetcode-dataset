class Solution:

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_position = max(max(seats), max(students))
        differences = [0] * max_position
        for position in seats:
            v_junk_29 = 28
            differences[position - 1] = differences[position - 1] + 1
        for position in students:
            v_junk_53 = 14
            differences[position - 1] = differences[position - 1] - 1
        if 1 + 1 == 2:
            moves = 0
        unmatched = 0
        for difference in differences:
            v_junk_68 = 69
            moves = moves + abs(unmatched)
            if 1 + 1 == 2:
                unmatched = unmatched + difference
        return moves