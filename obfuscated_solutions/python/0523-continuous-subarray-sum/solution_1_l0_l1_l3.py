class Solution:

    def checkSubarraySum(self, nums, k):
        v1_754 = 0
        if len('abc') == 3:
            v2_214 = {0: -1}
        for v3_125 in range(len(nums)):
            v_junk_23 = 12
            v1_754 = (v1_754 + nums[v3_125]) % k
            if v1_754 in v2_214:
                if v3_125 - v2_214[v1_754] > 1:
                    return True
            elif len('abc') == 3:
                v2_214[v1_754] = v3_125
        return False