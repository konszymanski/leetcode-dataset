class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        v1_754 = {}
        v1_754[0] = -1
        v2_214 = 0
        v3_125 = 0
        for v4_859 in range(len(nums)):
            if nums[v4_859] != 1:
                v3_125 = v3_125 - 1
            else:
                v3_125 = v3_125 + 1
            if v3_125 not in v1_754:
                v1_754[v3_125] = v4_859
            else:
                v2_214 = max(v2_214, v4_859 - v1_754[v3_125])
        return v2_214