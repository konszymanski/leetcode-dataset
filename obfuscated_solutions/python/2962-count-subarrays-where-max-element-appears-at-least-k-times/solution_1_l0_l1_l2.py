class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        v1_754 = max(nums)
        v2_214 = v3_125 = v4_859 = 0
        for v5_381 in range(len(nums)):
            if nums[v5_381] == v1_754:
                v4_859 = v4_859 + 1
            while v4_859 == k:
                if nums[v3_125] == v1_754:
                    v4_859 = v4_859 - 1
                v3_125 = v3_125 + 1
            v2_214 = v2_214 + v3_125
        return v2_214