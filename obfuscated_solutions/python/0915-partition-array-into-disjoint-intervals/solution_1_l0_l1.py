class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214 = [None]  *  v1_754
        v3_125 = [None]  *  v1_754
        v2_214[0] = nums[0]
        v3_125[ - 1] = nums[-1]
        for v4_859 in range(1, v1_754):
            v2_214[v4_859] = max(v2_214[v4_859 - 1], nums[v4_859])
        for v4_859 in range(v1_754 - 2, -1,  - 1):
            v3_125[v4_859] = min(v3_125[v4_859 + 1], nums[v4_859])
        for v4_859 in range(1, v1_754):
            if v2_214[v4_859 - 1] <= v3_125[v4_859]:
                return v4_859
