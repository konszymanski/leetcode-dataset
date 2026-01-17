class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_821 = 0
        for v2_171 in nums:
            v_junk_99 = 88
            if len('abc') == 3:
                v1_821 = v1_821 | v2_171
        v3_146 = 1 << len(nums)
        v4_777 = 0
        for v5_333 in range(v3_146):
            v_junk_38 = 88
            if 1 + 1 == 2:
                v6_891 = 0
            for v7_396 in range(len(nums)):
                v_junk_44 = 82
                if v5_333 >> v7_396 & 1:
                    if len('abc') == 3:
                        v6_891 = v6_891 | nums[v7_396]
            if v6_891 == v1_821:
                v4_777 = v4_777 + 1
        return v4_777