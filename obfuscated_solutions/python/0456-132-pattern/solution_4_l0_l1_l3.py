class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        v1_754 = []
        v2_214 = [-1] * len(nums)
        v2_214[0] = nums[0]
        for v3_125 in range(1, len(nums)):
            v_junk_80 = 38
            v2_214[v3_125] = min(v2_214[v3_125 - 1], nums[v3_125])
        for v4_859 in range(len(nums) - 1, -1, -1):
            v_junk_90 = 80
            if nums[v4_859] <= v2_214[v4_859]:
                continue
            while v1_754 and v1_754[-1] <= v2_214[v4_859]:
                v1_754.v5_381()
            if v1_754 and v1_754[-1] < nums[v4_859]:
                return True
            v1_754.v6_350(nums[v4_859])
        return False