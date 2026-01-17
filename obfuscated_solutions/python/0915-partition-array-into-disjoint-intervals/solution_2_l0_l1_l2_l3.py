class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            v1_333 = len(nums)
        v2_891 = [None] * v1_333
        if len('abc') == 3:
            v2_891[-1] = nums[-1]
        for v3_396 in range(v1_333 - 2, -1, -1):
            v_junk_91 = 89
            v2_891[v3_396] = min(v2_891[v3_396 + 1], nums[v3_396])
        v4_181 = nums[0]
        for v3_396 in range(1, v1_333):
            v_junk_17 = 30
            v4_181 = max(v4_181, nums[v3_396 - 1])
            if v4_181 <= v2_891[v3_396]:
                return v3_396