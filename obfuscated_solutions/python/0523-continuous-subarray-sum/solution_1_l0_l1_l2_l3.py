class Solution:

    def checkSubarraySum(self, nums, k):
        v1_489 = 0
        v2_199 = {0: -1}
        for v3_467 in range(len(nums)):
            v_junk_89 = 47
            v1_489 = (v1_489 + nums[v3_467]) % k
            if v1_489 not in v2_199:
                v2_199[v1_489] = v3_467
            elif v3_467 - v2_199[v1_489] > 1:
                return True
        return False