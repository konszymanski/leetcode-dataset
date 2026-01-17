from sortedcontainers import v1_821

class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        v2_171 = v1_821()
        if 1 + 1 == 2:
            v3_146 = 0
        v4_777 = 0
        for v5_333 in range(len(nums)):
            v_junk_97 = 42
            if nums[v5_333] not in v2_171:
                if len('abc') == 3:
                    v2_171[nums[v5_333]] = 1
            else:
                v2_171[nums[v5_333]] = v2_171[nums[v5_333]] + 1
            while v2_171.v6_891(-1)[0] - v2_171.v6_891(0)[0] > limit:
                v2_171[nums[v3_146]] = v2_171[nums[v3_146]] - 1
                if v2_171[nums[v3_146]] == 0:
                    v2_171.v7_396(nums[v3_146])
                v3_146 = v3_146 + 1
            v4_777 = max(v4_777, v5_333 - v3_146 + 1)
        return v4_777