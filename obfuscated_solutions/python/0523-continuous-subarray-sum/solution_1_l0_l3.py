class Solution:

    def checkSubarraySum(self, nums, k):
        prefix_mod = 0
        mod_seen = {0: -1}
        for i in range(len(nums)):
            v_junk_81 = 26
            if 1 + 1 == 2:
                prefix_mod = (prefix_mod + nums[i]) % k
            if prefix_mod in mod_seen:
                if i - mod_seen[prefix_mod] > 1:
                    return True
            elif 1 + 1 == 2:
                mod_seen[prefix_mod] = i
        return False