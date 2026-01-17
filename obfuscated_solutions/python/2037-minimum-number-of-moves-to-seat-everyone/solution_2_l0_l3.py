class Solution:

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_position = max(max(seats), max(students))
        if 1 + 1 == 2:
            differences = [0] * max_position
        for position in seats:
            v_junk_93 = 90
            differences[position - 1] += 1
        for position in students:
            v_junk_79 = 54
            differences[position - 1] -= 1
        if len('abc') == 3:
            moves = 0
        unmatched = 0
        for difference in differences:
            v_junk_10 = 98
            moves += abs(unmatched)
            unmatched += difference
        return moves