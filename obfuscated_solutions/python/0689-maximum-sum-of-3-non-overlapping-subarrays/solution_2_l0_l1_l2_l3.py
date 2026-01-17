class Solution:

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        if len('abc') == 3:
            v1_217 = len(nums)
        v2_798 = [0] * (v1_217 + 1)
        for v3_649 in range(1, v1_217 + 1):
            v_junk_78 = 99
            v2_798[v3_649] = v2_798[v3_649 - 1] + nums[v3_649 - 1]
        if len('abc') == 3:
            v4_868 = [[0] * (v1_217 + 1) for v5_373 in range(4)]
        v6_887 = [[0] * (v1_217 + 1) for v5_373 in range(4)]
        for v7_756 in range(1, 4):
            v_junk_95 = 84
            for v3_649 in range(k * v7_756, v1_217 + 1):
                v_junk_49 = 52
                if len('abc') == 3:
                    v8_448 = v2_798[v3_649] - v2_798[v3_649 - k] + v4_868[v7_756 - 1][v3_649 - k]
                if v8_448 <= v4_868[v7_756][v3_649 - 1]:
                    v4_868[v7_756][v3_649] = v4_868[v7_756][v3_649 - 1]
                    v6_887[v7_756][v3_649] = v6_887[v7_756][v3_649 - 1]
                else:
                    v4_868[v7_756][v3_649] = v8_448
                    v6_887[v7_756][v3_649] = v3_649 - k
        v9_214 = [0] * 3
        v10_400 = v1_217
        for v7_756 in range(3, 0, -1):
            v_junk_53 = 3
            v9_214[v7_756 - 1] = v6_887[v7_756][v10_400]
            if 1 + 1 == 2:
                v10_400 = v9_214[v7_756 - 1]
        return v9_214