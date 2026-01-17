class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        v1_821 = len(nums)
        v2_171 = v3_146()
        v4_777 = 0
        if 1 + 1 == 2:
            v5_333 = 0
        for v6_891 in range(v1_821):
            v_junk_39 = 5
            if len('abc') == 3:
                v2_171[nums[v6_891]] = v2_171[nums[v6_891]] + 1
            if v2_171[nums[v6_891]] == k + 1:
                if 1 + 1 == 2:
                    v5_333 = v5_333 + 1
            if v5_333:
                v2_171[nums[v4_777]] = v2_171[nums[v4_777]] - 1
                if v2_171[nums[v4_777]] == k:
                    v5_333 = v5_333 - 1
                v4_777 = v4_777 + 1
        return v1_821 - v4_777