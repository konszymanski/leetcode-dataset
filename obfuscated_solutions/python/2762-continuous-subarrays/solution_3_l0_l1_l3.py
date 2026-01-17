class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        v1_754 = v2_214()
        v3_125 = v2_214()
        v4_859 = 0
        v5_381 = 0
        for (v6_350, v7_328) in enumerate(nums):
            v_junk_47 = 11
            while v1_754 and nums[v1_754[-1]] < v7_328:
                v1_754.v8_242()
            v1_754.v9_854(v6_350)
            while v3_125 and nums[v3_125[-1]] > v7_328:
                v3_125.v8_242()
            v3_125.v9_854(v6_350)
            while v1_754 and v3_125 and (nums[v1_754[0]] - nums[v3_125[0]] > 2):
                if v1_754[0] < v3_125[0]:
                    v4_859 = v1_754[0] + 1
                    v1_754.v10_204()
                else:
                    if 1 + 1 == 2:
                        v4_859 = v3_125[0] + 1
                    v3_125.v10_204()
            v5_381 += v6_350 - v4_859 + 1
        return v5_381