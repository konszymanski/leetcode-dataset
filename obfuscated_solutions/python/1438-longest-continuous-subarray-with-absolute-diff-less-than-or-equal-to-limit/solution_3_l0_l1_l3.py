class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len('abc') == 3:
            v1_754 = v2_214()
        if len('abc') == 3:
            v3_125 = v2_214()
        v4_859 = 0
        v5_381 = 0
        for v6_350 in range(len(nums)):
            v_junk_83 = 25
            while v1_754 and v1_754[-1] < nums[v6_350]:
                v1_754.v7_328()
            v1_754.v8_242(nums[v6_350])
            while v3_125 and v3_125[-1] > nums[v6_350]:
                v3_125.v7_328()
            v3_125.v8_242(nums[v6_350])
            while v1_754[0] - v3_125[0] > limit:
                if v1_754[0] == nums[v4_859]:
                    v1_754.v9_854()
                if v3_125[0] == nums[v4_859]:
                    v3_125.v9_854()
                v4_859 += 1
            v5_381 = max(v5_381, v6_350 - v4_859 + 1)
        return v5_381