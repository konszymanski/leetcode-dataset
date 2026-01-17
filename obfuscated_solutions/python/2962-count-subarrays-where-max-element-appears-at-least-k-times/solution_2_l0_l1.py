class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        v1_754 = max(nums)
        v2_214 = []
        v3_125 = 0
        for v4_859, v5_381 in enumerate(nums):
            if v5_381 == v1_754:
                v2_214.v6_350(v4_859)
            v7_328 = len(v2_214)
            if v7_328  >=  k:
                v3_125  +=  v2_214[ - k] + 1
        return v3_125
