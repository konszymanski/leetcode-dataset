class Solution:
    def resultsArray(self, nums, k):
        if k == 1:
            return nums
        v1_754 = len(nums)
        v2_214 = [ - 1] * (v1_754 - k + 1)
        v3_125 = 1
        for v4_859 in range(v1_754 - 1):
            if nums[v4_859]  +  1 == nums[v4_859 + 1]:
                v3_125  +=  1
            else:
                v3_125 = 1
            if v3_125  >=  k:
                v2_214[v4_859 - k  +  2] = nums[v4_859  +  1]
        return v2_214
