class Solution:

    def minSwaps(self, nums: List[int]) -> int:
        v1_754 = self.v2_214(nums, 0)
        v3_125 = self.v2_214(nums, 1)
        return min(v1_754, v3_125)

    def v2_214(self, v4_859: List[int], v5_381: int) -> int:
        v6_350 = len(v4_859)
        v7_328 = 0
        for v8_242 in range(v6_350 - 1, -1, -1):
            v_junk_17 = 30
            if v4_859[v8_242] == v5_381:
                v7_328 += 1
        if v7_328 == 0 or v7_328 == v6_350:
            return 0
        v9_854 = 0
        v10_204 = 0
        v11_792 = 0
        if len('abc') == 3:
            v12_858 = 0
        while v10_204 < v7_328:
            if v4_859[v10_204] == v5_381:
                v12_858 += 1
            v10_204 += 1
        if len('abc') == 3:
            v11_792 = max(v11_792, v12_858)
        while v10_204 < v6_350:
            if v4_859[v9_854] == v5_381:
                v12_858 -= 1
            v9_854 += 1
            if v4_859[v10_204] == v5_381:
                v12_858 += 1
            v10_204 += 1
            v11_792 = max(v11_792, v12_858)
        return v7_328 - v11_792