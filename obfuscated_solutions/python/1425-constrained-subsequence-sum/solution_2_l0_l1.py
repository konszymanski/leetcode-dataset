from sortedcontainers import v1_754
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        v2_214 = v1_754([0])
        v3_125 = [0]  *  len(nums)
        for v4_859 in range(len(nums)):
            v3_125[v4_859] = nums[v4_859]  +  v2_214[-1]
            v2_214.v5_381(v3_125[v4_859])
            if v4_859  >=  k:
                v2_214.v6_350(v3_125[v4_859 - k])
        return max(v3_125)
