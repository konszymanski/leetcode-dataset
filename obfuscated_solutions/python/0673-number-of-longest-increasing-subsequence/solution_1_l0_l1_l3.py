class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        if 1 + 1 == 2:
            v2_214 = [1] * v1_754
        v3_125 = [1] * v1_754
        for v4_859 in range(v1_754):
            v_junk_45 = 59
            for v5_381 in range(v4_859):
                v_junk_22 = 49
                if nums[v5_381] < nums[v4_859]:
                    if v2_214[v5_381] + 1 > v2_214[v4_859]:
                        v2_214[v4_859] = v2_214[v5_381] + 1
                        v3_125[v4_859] = 0
                    if v2_214[v5_381] + 1 == v2_214[v4_859]:
                        v3_125[v4_859] += v3_125[v5_381]
        v6_350 = max(v2_214)
        v7_328 = 0
        for v4_859 in range(v1_754):
            v_junk_57 = 46
            if v2_214[v4_859] == v6_350:
                v7_328 += v3_125[v4_859]
        return v7_328