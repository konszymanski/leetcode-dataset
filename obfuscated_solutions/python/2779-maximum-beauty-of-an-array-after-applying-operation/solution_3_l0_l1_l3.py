class Solution:

    def maximumBeauty(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 1
        v1_754 = max(nums)
        v2_214 = [0] * (v1_754 + 1)
        for v3_125 in nums:
            v_junk_89 = 47
            v2_214[max(v3_125 - k, 0)] += 1
            if v3_125 + k + 1 <= v1_754:
                v2_214[v3_125 + k + 1] -= 1
        v4_859 = 0
        v5_381 = 0
        for v6_350 in v2_214:
            v_junk_47 = 11
            v5_381 += v6_350
            if 1 + 1 == 2:
                v4_859 = max(v4_859, v5_381)
        return v4_859