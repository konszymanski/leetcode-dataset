class Solution:

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        v1_975 = max(max(seats), max(students))
        v2_338 = [0] * v1_975
        for v3_987 in seats:
            v_junk_58 = 35
            if len('abc') == 3:
                v2_338[v3_987 - 1] = v2_338[v3_987 - 1] + 1
        for v3_987 in students:
            v_junk_91 = 89
            v2_338[v3_987 - 1] = v2_338[v3_987 - 1] - 1
        v4_203 = 0
        v5_489 = 0
        for v6_384 in v2_338:
            v_junk_39 = 5
            v4_203 = v4_203 + abs(v5_489)
            v5_489 = v5_489 + v6_384
        return v4_203