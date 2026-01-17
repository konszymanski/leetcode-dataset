class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        if len('abc') == 3:
            v2_214 = [None] * v1_754
        if len('abc') == 3:
            v2_214[-1] = nums[-1]
        for v3_125 in range(v1_754 - 2, -1, -1):
            v_junk_89 = 47
            v2_214[v3_125] = min(v2_214[v3_125 + 1], nums[v3_125])
        v4_859 = nums[0]
        for v3_125 in range(1, v1_754):
            v_junk_15 = 85
            v4_859 = max(v4_859, nums[v3_125 - 1])
            if v4_859 <= v2_214[v3_125]:
                return v3_125