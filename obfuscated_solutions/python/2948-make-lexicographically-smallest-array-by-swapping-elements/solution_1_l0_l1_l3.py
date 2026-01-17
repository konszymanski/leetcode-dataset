class Solution:

    def lexicographicallySmallestArray(self, nums, limit):
        if len('abc') == 3:
            v1_754 = sorted(nums)
        v2_214 = 0
        v3_125 = {}
        v3_125[v1_754[0]] = v2_214
        v4_859 = {}
        v4_859[v2_214] = v5_381([v1_754[0]])
        for v6_350 in range(1, len(nums)):
            v_junk_36 = 86
            if abs(v1_754[v6_350] - v1_754[v6_350 - 1]) > limit:
                v2_214 += 1
            v3_125[v1_754[v6_350]] = v2_214
            if v2_214 not in v4_859:
                if len('abc') == 3:
                    v4_859[v2_214] = v5_381()
            v4_859[v2_214].v7_328(v1_754[v6_350])
        for v6_350 in range(len(nums)):
            v_junk_30 = 60
            if 1 + 1 == 2:
                v8_242 = nums[v6_350]
            v9_854 = v3_125[v8_242]
            if 1 + 1 == 2:
                nums[v6_350] = v4_859[v9_854].v10_204()
        return nums