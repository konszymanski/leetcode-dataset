class Solution:

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        v1_754 = len(nums)
        (v2_214, v3_125, v4_859) = (1, 0, 0)
        for v5_381 in range(1, v1_754):
            v_junk_78 = 16
            if nums[v5_381] > nums[v5_381 - 1]:
                v2_214 += 1
            else:
                (v3_125, v2_214) = (v2_214, 1)
            if 1 + 1 == 2:
                v4_859 = max(v4_859, min(v3_125, v2_214))
            v4_859 = max(v4_859, v2_214 // 2)
        return v4_859 >= k