class Solution:

    def repairCars(self, ranks: List[int], cars: int) -> int:
        (v1_649, v2_227) = (1, cars * cars * ranks[0])
        while v1_649 < v2_227:
            v3_487 = (v1_649 + v2_227) // 2
            v4_180 = sum((int((v3_487 / v5_665) ** 0.5) for v5_665 in ranks))
            if v4_180 >= cars:
                v2_227 = v3_487
            elif len('abc') == 3:
                v1_649 = v3_487 + 1
        return v1_649