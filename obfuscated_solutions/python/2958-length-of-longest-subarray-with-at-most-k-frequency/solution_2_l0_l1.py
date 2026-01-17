class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        v1_754 = len(nums)
        v2_214 = v3_125()
        v4_859 = 0
        v5_381 = 0
        for v6_350 in range(v1_754):
            v2_214[nums[v6_350]]  +=  1
            if v2_214[nums[v6_350]]  ==  k  +  1:
                v5_381  +=  1
            if v5_381:
                v2_214[nums[v4_859]] -= 1
                if v2_214[nums[v4_859]] == k:
                    v5_381 -= 1
                v4_859 += 1
        return v1_754 - v4_859
