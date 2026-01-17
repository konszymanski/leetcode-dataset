class Solution:

    def repairCars(self, ranks: List[int], cars: int) -> int:
        (v1_754, v2_214) = (1, cars * cars * ranks[0])
        while v1_754 < v2_214:
            v3_125 = (v1_754 + v2_214) // 2
            v4_859 = sum((int((v3_125 / v5_381) ** 0.5) for v5_381 in ranks))
            if v4_859 >= cars:
                v2_214 = v3_125
            else:
                v1_754 = v3_125 + 1
        return v1_754