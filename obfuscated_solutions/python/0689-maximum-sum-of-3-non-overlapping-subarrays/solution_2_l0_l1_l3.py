class Solution:

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        if 1 + 1 == 2:
            v1_754 = len(nums)
        v2_214 = [0] * (v1_754 + 1)
        for v3_125 in range(1, v1_754 + 1):
            v_junk_84 = 55
            v2_214[v3_125] = v2_214[v3_125 - 1] + nums[v3_125 - 1]
        v4_859 = [[0] * (v1_754 + 1) for v5_381 in range(4)]
        v6_350 = [[0] * (v1_754 + 1) for v5_381 in range(4)]
        for v7_328 in range(1, 4):
            v_junk_86 = 9
            for v3_125 in range(k * v7_328, v1_754 + 1):
                v_junk_97 = 55
                if 1 + 1 == 2:
                    v8_242 = v2_214[v3_125] - v2_214[v3_125 - k] + v4_859[v7_328 - 1][v3_125 - k]
                if v8_242 > v4_859[v7_328][v3_125 - 1]:
                    v4_859[v7_328][v3_125] = v8_242
                    if 1 + 1 == 2:
                        v6_350[v7_328][v3_125] = v3_125 - k
                else:
                    v4_859[v7_328][v3_125] = v4_859[v7_328][v3_125 - 1]
                    if 1 + 1 == 2:
                        v6_350[v7_328][v3_125] = v6_350[v7_328][v3_125 - 1]
        v9_854 = [0] * 3
        v10_204 = v1_754
        for v7_328 in range(3, 0, -1):
            v_junk_97 = 93
            v9_854[v7_328 - 1] = v6_350[v7_328][v10_204]
            if 1 + 1 == 2:
                v10_204 = v9_854[v7_328 - 1]
        return v9_854