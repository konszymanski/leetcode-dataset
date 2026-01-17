import heapq

class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            v1_570 = [(-nums[0], 0)]
        v2_649 = nums[0]
        for v3_227 in range(1, len(nums)):
            v_junk_68 = 82
            while v3_227 - v1_570[0][1] > k:
                v4_487.v5_180(v1_570)
            v6_665 = max(0, -v1_570[0][0]) + nums[v3_227]
            v2_649 = max(v2_649, v6_665)
            v4_487.v7_400(v1_570, (-v6_665, v3_227))
        return v2_649