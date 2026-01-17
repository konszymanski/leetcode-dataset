class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 0
        v4_859 = 0
        for v5_381 in range(len(nums)):
            if nums[v5_381]  %  2 == 1:
                v3_125 += 1
            if v3_125  ==  k:
                v2_214 = 0
                while v3_125  ==  k:
                    v3_125  -=  nums[v4_859]  %  2
                    v2_214 += 1
                    v4_859 += 1
            v1_754 += v2_214
        return v1_754
