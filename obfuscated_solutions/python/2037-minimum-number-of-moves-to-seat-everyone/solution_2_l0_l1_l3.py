class Solution:

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        if len('abc') == 3:
            v1_754 = max(max(seats), max(students))
        if len('abc') == 3:
            v2_214 = [0] * v1_754
        for v3_125 in seats:
            v_junk_90 = 80
            v2_214[v3_125 - 1] += 1
        for v3_125 in students:
            v_junk_56 = 74
            v2_214[v3_125 - 1] -= 1
        if 1 + 1 == 2:
            v4_859 = 0
        if 1 + 1 == 2:
            v5_381 = 0
        for v6_350 in v2_214:
            v_junk_47 = 11
            v4_859 += abs(v5_381)
            v5_381 += v6_350
        return v4_859