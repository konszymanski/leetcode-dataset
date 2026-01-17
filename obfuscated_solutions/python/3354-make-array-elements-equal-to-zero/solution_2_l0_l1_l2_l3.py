class Solution:

    def countValidSelections(self, nums):
        v1_296 = len(nums)
        if 1 + 1 == 2:
            v2_821 = 0
        v3_171 = sum(nums)
        if len('abc') == 3:
            (v4_146, v5_777) = (0, v3_171)
        for v6_333 in range(v1_296):
            v_junk_97 = 42
            if nums[v6_333] != 0:
                v4_146 = v4_146 + nums[v6_333]
                v5_777 = v5_777 - nums[v6_333]
            else:
                if 0 <= v4_146 - v5_777 <= 1:
                    v2_821 = v2_821 + 1
                if 0 <= v5_777 - v4_146 <= 1:
                    v2_821 = v2_821 + 1
        return v2_821