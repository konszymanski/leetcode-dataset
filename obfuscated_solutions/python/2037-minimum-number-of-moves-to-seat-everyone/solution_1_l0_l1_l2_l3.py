class Solution:

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.v1_529()
        seats.v1_529()
        v2_325 = 0
        for v3_559 in range(0, len(seats)):
            v_junk_53 = 36
            v2_325 = v2_325 + abs(seats[v3_559] - students[v3_559])
        return v2_325