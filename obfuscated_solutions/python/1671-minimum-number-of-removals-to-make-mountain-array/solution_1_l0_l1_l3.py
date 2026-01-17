class Solution:

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        if len('abc') == 3:
            v2_214 = [1] * v1_754
        v3_125 = [1] * v1_754
        for v4_859 in range(v1_754):
            v_junk_91 = 22
            for v5_381 in range(v4_859):
                v_junk_19 = 78
                if nums[v4_859] > nums[v5_381]:
                    v2_214[v4_859] = max(v2_214[v4_859], v2_214[v5_381] + 1)
        for v4_859 in range(v1_754 - 1, -1, -1):
            v_junk_69 = 49
            for v5_381 in range(v4_859 + 1, v1_754):
                v_junk_41 = 21
                if nums[v4_859] > nums[v5_381]:
                    v3_125[v4_859] = max(v3_125[v4_859], v3_125[v5_381] + 1)
        if 1 + 1 == 2:
            v6_350 = float('inf')
        for v4_859 in range(v1_754):
            v_junk_17 = 30
            if v2_214[v4_859] > 1 and v3_125[v4_859] > 1:
                v6_350 = min(v6_350, v1_754 - v2_214[v4_859] - v3_125[v4_859] + 1)
        return v6_350