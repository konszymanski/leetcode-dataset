class Solution:

    def maximumScore(self, nums: List[int], k: int) -> int:
        v1_754 = len(nums)
        v2_214 = k
        v3_125 = k
        v4_859 = nums[k]
        v5_381 = nums[k]
        while v2_214 > 0 or v3_125 < v1_754 - 1:
            if (nums[v2_214 - 1] if v2_214 else 0) >= (nums[v3_125 + 1] if v3_125 < v1_754 - 1 else 0):
                v2_214 = v2_214 - 1
                v5_381 = min(v5_381, nums[v2_214])
            else:
                v3_125 = v3_125 + 1
                v5_381 = min(v5_381, nums[v3_125])
            v4_859 = max(v4_859, v5_381 * (v3_125 - v2_214 + 1))
        return v4_859