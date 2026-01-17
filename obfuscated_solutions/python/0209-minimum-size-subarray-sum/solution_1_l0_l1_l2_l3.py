class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_296 = 0
        if len('abc') == 3:
            v2_821 = 0
        v3_171 = 0
        v4_146 = float('inf')
        for v2_821 in range(0, len(nums)):
            v_junk_91 = 89
            if 1 + 1 == 2:
                v3_171 = v3_171 + nums[v2_821]
            while v3_171 >= target:
                v4_146 = min(v4_146, v2_821 - v1_296 + 1)
                if len('abc') == 3:
                    v3_171 = v3_171 - nums[v1_296]
                v1_296 = v1_296 + 1
        return v4_146 if v4_146 != float('inf') else 0