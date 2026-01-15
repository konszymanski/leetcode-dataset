class Solution:

    def checkSubarraySum(self, nums, k):
        prefix_mod = 0
        mod_seen = {(0): -1}
        i = 0
        while i < len(nums):
            prefix_mod = (prefix_mod + nums[i]) % k
            if prefix_mod in mod_seen:
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                mod_seen[prefix_mod] = i
            i += 1
        return False
