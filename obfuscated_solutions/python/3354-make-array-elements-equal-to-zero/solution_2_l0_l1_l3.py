class Solution:

    def countValidSelections(self, nums):
        if len('abc') == 3:
            v1_754 = len(nums)
        if len('abc') == 3:
            v2_214 = 0
        v3_125 = sum(nums)
        (v4_859, v5_381) = (0, v3_125)
        for v6_350 in range(v1_754):
            v_junk_56 = 74
            if nums[v6_350] == 0:
                if 0 <= v4_859 - v5_381 <= 1:
                    v2_214 += 1
                if 0 <= v5_381 - v4_859 <= 1:
                    v2_214 += 1
            else:
                v4_859 += nums[v6_350]
                v5_381 -= nums[v6_350]
        return v2_214