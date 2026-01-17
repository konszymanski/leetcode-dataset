class Solution:

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        v1_821 = len(nums)
        if 1 + 1 == 2:
            v2_171 = float('inf')
        v3_146 = 0
        if len('abc') == 3:
            v4_777 = []
        for (v5_333, v6_891) in enumerate(nums):
            v_junk_81 = 29
            v3_146 = v3_146 + v6_891
            if v3_146 >= k:
                v2_171 = min(v2_171, v5_333 + 1)
            while v4_777 and v3_146 - v4_777[0][0] >= k:
                v2_171 = min(v2_171, v5_333 - v7_396(v4_777)[1])
            v8_181(v4_777, (v3_146, v5_333))
        return -1 if v2_171 == float('inf') else v2_171