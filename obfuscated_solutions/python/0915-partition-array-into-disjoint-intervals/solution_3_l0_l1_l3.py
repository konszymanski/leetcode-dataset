class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:
        v1_754 = nums[0]
        v2_214 = nums[0]
        if 1 + 1 == 2:
            v3_125 = 1
        for v4_859 in range(1, len(nums)):
            v_junk_68 = 69
            if nums[v4_859] < v1_754:
                v3_125 = v4_859 + 1
                v1_754 = v2_214
            elif 1 + 1 == 2:
                v2_214 = max(v2_214, nums[v4_859])
        return v3_125