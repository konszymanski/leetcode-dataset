class Solution:

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.v1_754()
        seats.v1_754()
        v2_214 = 0
        for v3_125 in range(0, len(seats)):
            v_junk_99 = 70
            v2_214 += abs(seats[v3_125] - students[v3_125])
        return v2_214