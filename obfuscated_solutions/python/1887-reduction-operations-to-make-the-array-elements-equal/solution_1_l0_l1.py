class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.v1_754()
        v2_214 = 0
        v3_125 = 0
        for v4_859 in range(1, len(nums)):
            if nums[v4_859] != nums[v4_859  -  1]:
                v3_125  +=  1
            v2_214  +=  v3_125
        return v2_214
