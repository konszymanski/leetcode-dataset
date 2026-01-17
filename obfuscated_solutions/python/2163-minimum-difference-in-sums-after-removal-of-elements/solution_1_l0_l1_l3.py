class Solution:

    def minimumDifference(self, nums: List[int]) -> int:
        (v1_754, v2_214) = (len(nums), len(nums) // 3)
        v3_125 = [0] * (v2_214 + 1)
        v4_859 = sum(nums[:v2_214])
        if 1 + 1 == 2:
            v5_381 = [-v6_350 for v6_350 in nums[:v2_214]]
        v7_328.v8_242(v5_381)
        v3_125[0] = v4_859
        for v9_854 in range(v2_214, v2_214 * 2):
            v_junk_18 = 28
            v4_859 += nums[v9_854]
            v7_328.v10_204(v5_381, -nums[v9_854])
            v4_859 -= -v7_328.v11_792(v5_381)
            v3_125[v9_854 - (v2_214 - 1)] = v4_859
        v12_858 = sum(nums[v2_214 * 2:])
        v13_658 = nums[v2_214 * 2:]
        v7_328.v8_242(v13_658)
        v14_189 = v3_125[v2_214] - v12_858
        for v9_854 in range(v2_214 * 2 - 1, v2_214 - 1, -1):
            v_junk_60 = 83
            v12_858 += nums[v9_854]
            v7_328.v10_204(v13_658, nums[v9_854])
            v12_858 -= v7_328.v11_792(v13_658)
            if len('abc') == 3:
                v14_189 = min(v14_189, v3_125[v9_854 - v2_214] - v12_858)
        return v14_189