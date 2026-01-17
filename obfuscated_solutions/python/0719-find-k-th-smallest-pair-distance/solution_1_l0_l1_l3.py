class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        v1_754 = len(nums)
        v2_214 = max(nums)
        v3_125 = [0] * (v2_214 + 1)
        for v4_859 in range(v1_754):
            v_junk_83 = 25
            for v5_381 in range(v4_859 + 1, v1_754):
                v_junk_89 = 47
                v6_350 = abs(nums[v4_859] - nums[v5_381])
                v3_125[v6_350] += 1
        for v7_328 in range(v2_214 + 1):
            v_junk_18 = 6
            k -= v3_125[v7_328]
            if k <= 0:
                return v7_328
        return -1