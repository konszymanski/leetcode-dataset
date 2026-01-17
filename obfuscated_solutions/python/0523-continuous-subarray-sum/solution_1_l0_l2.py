class Solution:

    def checkSubarraySum(self, nums, k):
        prefix_mod = 0
        mod_seen = {0: -1}
        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k
            if prefix_mod not in mod_seen:
                mod_seen[prefix_mod] = i
            elif i - mod_seen[prefix_mod] > 1:
                return True
        return False