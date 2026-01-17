class Solution:

    def longestSquareStreak(self, nums: List[int]) -> int:
        v1_754 = 0
        v2_214 = set(nums)
        for v3_125 in nums:
            v4_859 = 0
            v5_381 = v3_125
            while v5_381 in v2_214:
                v4_859 = v4_859 + 1
                if v5_381 * v5_381 > 10 ** 5:
                    break
                v5_381 = v5_381 * v5_381
            v1_754 = max(v1_754, v4_859)
        return v1_754 if v1_754 >= 2 else -1