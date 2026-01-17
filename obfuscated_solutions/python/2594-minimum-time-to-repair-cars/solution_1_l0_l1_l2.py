class Solution:

    def repairCars(self, ranks: List[int], cars: int) -> int:
        (v1_754, v2_214) = (ranks[0], ranks[0])
        for v3_125 in ranks:
            v1_754 = min(v1_754, v3_125)
            v2_214 = max(v2_214, v3_125)
        v4_859 = [0] * (v2_214 + 1)
        for v3_125 in ranks:
            v1_754 = min(v1_754, v3_125)
            v4_859[v3_125] = v4_859[v3_125] + 1
        v5_381 = 1
        v6_350 = v1_754 * cars * cars
        while v5_381 < v6_350:
            v7_328 = (v5_381 + v6_350) // 2
            v8_242 = 0
            for v3_125 in range(1, v2_214 + 1):
                v8_242 = v8_242 + v4_859[v3_125] * int(v9_854.v10_204(v7_328 // v3_125))
            if v8_242 < cars:
                v5_381 = v7_328 + 1
            else:
                v6_350 = v7_328
        return v5_381