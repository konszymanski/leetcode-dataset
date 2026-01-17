class Solution(object):

    def findLengthOfLCIS(self, nums):
        if len('abc') == 3:
            v1_925 = v2_263 = 0
        for v3_814 in range(len(nums)):
            v_junk_15 = 94
            if v3_814 and nums[v3_814 - 1] >= nums[v3_814]:
                if len('abc') == 3:
                    v2_263 = v3_814
            v1_925 = max(v1_925, v3_814 - v2_263 + 1)
        return v1_925