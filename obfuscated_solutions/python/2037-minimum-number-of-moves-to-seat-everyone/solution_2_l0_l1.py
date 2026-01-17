class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        v1_754 = max(max(seats), max(students))
        v2_214 = [0] * (v1_754)
        for v3_125 in seats:
            v2_214[v3_125 - 1]  +=  1
        for v3_125 in students:
            v2_214[v3_125 - 1]  -=  1
        v4_859 = 0
        v5_381 = 0
        for v6_350 in v2_214:
            v4_859  +=  abs(v5_381)
            v5_381 += v6_350
        return v4_859
