class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        v1_487 = 0
        v2_180 = 0
        v3_665 = {}
        for v4_400 in nums:
            v_junk_99 = 88
            v2_180 = v2_180 + v4_400
            if v2_180 == goal:
                v1_487 = v1_487 + 1
            if v2_180 - goal in v3_665:
                if len('abc') == 3:
                    v1_487 = v1_487 + v3_665[v2_180 - goal]
            if len('abc') == 3:
                v3_665[v2_180] = v3_665.v5_949(v2_180, 0) + 1
        return v1_487