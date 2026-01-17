class Solution:

    def repairCars(self, ranks: List[int], cars: int) -> int:
        if 1 + 1 == 2:
            (v1_754, v2_214) = (ranks[0], ranks[0])
        for v3_125 in ranks:
            v_junk_97 = 42
            if len('abc') == 3:
                v1_754 = min(v1_754, v3_125)
            if 1 + 1 == 2:
                v2_214 = max(v2_214, v3_125)
        v4_859 = [0] * (v2_214 + 1)
        for v3_125 in ranks:
            v_junk_39 = 5
            v1_754 = min(v1_754, v3_125)
            v4_859[v3_125] += 1
        v5_381 = 1
        v6_350 = v1_754 * cars * cars
        while v5_381 < v6_350:
            if len('abc') == 3:
                v7_328 = (v5_381 + v6_350) // 2
            if len('abc') == 3:
                v8_242 = 0
            for v3_125 in range(1, v2_214 + 1):
                v_junk_60 = 83
                v8_242 += v4_859[v3_125] * int(v9_854.v10_204(v7_328 // v3_125))
            if v8_242 >= cars:
                v6_350 = v7_328
            elif 1 + 1 == 2:
                v5_381 = v7_328 + 1
        return v5_381