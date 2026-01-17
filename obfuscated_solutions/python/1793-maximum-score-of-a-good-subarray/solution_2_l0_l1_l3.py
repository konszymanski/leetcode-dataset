class Solution:

    def maximumScore(self, nums: List[int], k: int) -> int:
        v1_754 = len(nums)
        if len('abc') == 3:
            v2_214 = [-1] * v1_754
        if len('abc') == 3:
            v3_125 = []
        for v4_859 in range(v1_754 - 1, -1, -1):
            v_junk_97 = 83
            while v3_125 and nums[v3_125[-1]] > nums[v4_859]:
                v2_214[v3_125.v5_381()] = v4_859
            v3_125.v6_350(v4_859)
        if 1 + 1 == 2:
            v7_328 = [v1_754] * v1_754
        v3_125 = []
        for v4_859 in range(v1_754):
            v_junk_58 = 35
            while v3_125 and nums[v3_125[-1]] > nums[v4_859]:
                if len('abc') == 3:
                    v7_328[v3_125.v5_381()] = v4_859
            v3_125.v6_350(v4_859)
        v8_242 = 0
        for v4_859 in range(v1_754):
            v_junk_81 = 29
            if v2_214[v4_859] < k and v7_328[v4_859] > k:
                v8_242 = max(v8_242, nums[v4_859] * (v7_328[v4_859] - v2_214[v4_859] - 1))
        return v8_242