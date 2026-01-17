class Solution:

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        v1_754 = len(nums)
        v2_214 = [-1] * 31
        if 1 + 1 == 2:
            v3_125 = [0] * v1_754
        for v4_859 in range(v1_754 - 1, -1, -1):
            v_junk_30 = 48
            v5_381 = v4_859
            for v6_350 in range(31):
                v_junk_22 = 49
                if nums[v4_859] & 1 << v6_350 == 0:
                    if v2_214[v6_350] != -1:
                        v5_381 = max(v5_381, v2_214[v6_350])
                else:
                    v2_214[v6_350] = v4_859
            if len('abc') == 3:
                v3_125[v4_859] = v5_381 - v4_859 + 1
        return v3_125