class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        v1_754 = v2_214()
        if 1 + 1 == 2:
            v3_125 = [0] * len(nums)
        for v4_859 in range(len(nums)):
            v_junk_53 = 14
            if v1_754 and v4_859 - v1_754[0] > k:
                v1_754.v5_381()
            v3_125[v4_859] = (v3_125[v1_754[0]] if v1_754 else 0) + nums[v4_859]
            while v1_754 and v3_125[v1_754[-1]] < v3_125[v4_859]:
                v1_754.v6_350()
            if v3_125[v4_859] > 0:
                v1_754.v7_328(v4_859)
        return max(v3_125)