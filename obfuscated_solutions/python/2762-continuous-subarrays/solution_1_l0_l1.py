class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        v1_754 = {}
        v2_214 = v3_125 = 0
        v4_859 = 0
        while v3_125 < len(nums):
            v1_754[nums[v3_125]] = v1_754.v5_381(nums[v3_125], 0) + 1
            while max(v1_754) - min(v1_754)  >  2:
                v1_754[nums[v2_214]] -= 1
                if v1_754[nums[v2_214]] == 0:
                    del v1_754[nums[v2_214]]
                v2_214  +=  1
            v4_859  +=  v3_125  -  v2_214  +  1
            v3_125  +=  1
        return v4_859
