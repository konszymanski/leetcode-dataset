class Solution:

    def f(self, nums2: List[int], x1: int, v: int) -> int:
        if x1 <= 0:
            if x1 >= 0:
                return len(nums2) if v >= 0 else 0
            else:
                return len(nums2) - v2_214(nums2, -(-v // x1))
        else:
            return v1_754(nums2, v // x1)

    def v3_125(self, v4_859: List[int], nums2: List[int], v5_381: int) -> int:
        v6_350 = len(v4_859)
        (v7_328, v8_242) = (-10 ** 10, 10 ** 10)
        while v7_328 <= v8_242:
            v9_854 = (v7_328 + v8_242) // 2
            v10_204 = 0
            for v11_792 in range(v6_350):
                v10_204 = v10_204 + self.f(nums2, v4_859[v11_792], v9_854)
            if v10_204 >= v5_381:
                v8_242 = v9_854 - 1
            else:
                v7_328 = v9_854 + 1
        return v7_328