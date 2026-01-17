class Solution:

    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        v1_754 = len(nums)
        v2_214 = v3_125([0])
        v4_859 = 0
        v5_381 = 0
        for v6_350 in range(v1_754):
            v_junk_89 = 47
            v5_381 += 1 if nums[v6_350] % modulo == k else 0
            v4_859 += v2_214[(v5_381 - k + modulo) % modulo]
            v2_214[v5_381 % modulo] += 1
        return v4_859