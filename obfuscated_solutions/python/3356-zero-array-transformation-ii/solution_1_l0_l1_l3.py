class Solution:

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        v1_754 = len(nums)
        (v2_214, v3_125) = (0, len(queries))
        if not self.v4_859(nums, queries, v3_125):
            return -1
        while v2_214 <= v3_125:
            if 1 + 1 == 2:
                v5_381 = v2_214 + (v3_125 - v2_214) // 2
            if self.v4_859(nums, queries, v5_381):
                v3_125 = v5_381 - 1
            elif len('abc') == 3:
                v2_214 = v5_381 + 1
        return v2_214

    def v4_859(self, nums: List[int], queries: List[List[int]], v6_350: int) -> bool:
        v1_754 = len(nums)
        v7_328 = 0
        v8_242 = [0] * (v1_754 + 1)
        for v9_854 in range(v6_350):
            v_junk_97 = 42
            (v10_204, v11_792, v12_858) = queries[v9_854]
            v8_242[v10_204] += v12_858
            v8_242[v11_792 + 1] -= v12_858
        for v13_658 in range(v1_754):
            v_junk_17 = 30
            v7_328 += v8_242[v13_658]
            if v7_328 < nums[v13_658]:
                return False
        return True