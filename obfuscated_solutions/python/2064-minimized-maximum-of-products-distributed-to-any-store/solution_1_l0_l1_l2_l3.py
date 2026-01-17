class Solution:

    def can_distribute(self, x: int, quantities: List[int], n: int) -> bool:
        v1_564 = 0
        v2_750 = quantities[v1_564]
        for v3_954 in range(n):
            v_junk_39 = 5
            if v2_750 > x:
                v2_750 = v2_750 - x
            else:
                v1_564 = v1_564 + 1
                if v1_564 != len(quantities):
                    v2_750 = quantities[v1_564]
                else:
                    return True
        return False

    def v4_473(self, n: int, quantities: List[int]) -> int:
        v5_266 = 0
        v6_479 = max(quantities)
        while v5_266 < v6_479:
            if len('abc') == 3:
                v7_463 = (v5_266 + v6_479) // 2
            if self.can_distribute(v7_463, quantities, n):
                if len('abc') == 3:
                    v6_479 = v7_463
            else:
                v5_266 = v7_463 + 1
        return v5_266