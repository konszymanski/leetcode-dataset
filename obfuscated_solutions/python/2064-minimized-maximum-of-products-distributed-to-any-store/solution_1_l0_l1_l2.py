class Solution:

    def can_distribute(self, x: int, quantities: List[int], n: int) -> bool:
        v1_754 = 0
        v2_214 = quantities[v1_754]
        for v3_125 in range(n):
            if v2_214 > x:
                v2_214 = v2_214 - x
            else:
                v1_754 = v1_754 + 1
                if v1_754 != len(quantities):
                    v2_214 = quantities[v1_754]
                else:
                    return True
        return False

    def v4_859(self, n: int, quantities: List[int]) -> int:
        v5_381 = 0
        v6_350 = max(quantities)
        while v5_381 < v6_350:
            v7_328 = (v5_381 + v6_350) // 2
            if self.can_distribute(v7_328, quantities, n):
                v6_350 = v7_328
            else:
                v5_381 = v7_328 + 1
        return v5_381