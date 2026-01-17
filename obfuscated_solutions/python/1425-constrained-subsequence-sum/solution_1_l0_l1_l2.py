import heapq

class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        v1_754 = [(-nums[0], 0)]
        v2_214 = nums[0]
        for v3_125 in range(1, len(nums)):
            while v3_125 - v1_754[0][1] > k:
                v4_859.v5_381(v1_754)
            v6_350 = max(0, -v1_754[0][0]) + nums[v3_125]
            v2_214 = max(v2_214, v6_350)
            v4_859.v7_328(v1_754, (-v6_350, v3_125))
        return v2_214