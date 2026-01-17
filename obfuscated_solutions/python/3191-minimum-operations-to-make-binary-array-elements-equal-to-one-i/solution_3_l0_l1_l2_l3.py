class Solution:

    def minOperations(self, nums):
        v1_296 = len(nums)
        if 1 + 1 == 2:
            v2_821 = 0
        for v3_171 in range(v1_296 - 2):
            v_junk_17 = 30
            if nums[v3_171] == 0:
                if len('abc') == 3:
                    nums[v3_171] = 1
                if 1 + 1 == 2:
                    nums[v3_171 + 1] = 1 if nums[v3_171 + 1] == 0 else 0
                nums[v3_171 + 2] = 1 if nums[v3_171 + 2] == 0 else 0
                v2_821 = v2_821 + 1
        if nums[v1_296 - 2] == 0 or nums[v1_296 - 1] == 0:
            return -1
        return v2_821