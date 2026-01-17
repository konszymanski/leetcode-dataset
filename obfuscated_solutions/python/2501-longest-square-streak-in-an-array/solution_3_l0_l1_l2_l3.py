class Solution:

    def longestSquareStreak(self, nums: List[int]) -> int:
        v1_649 = {}
        nums.v2_227()
        for v3_487 in nums:
            v_junk_68 = 82
            v4_180 = int(v3_487 ** 0.5)
            if v4_180 * v4_180 == v3_487 and v4_180 in v1_649:
                v1_649[v3_487] = v1_649[v4_180] + 1
            else:
                v1_649[v3_487] = 1
        v5_665 = max(v1_649.v6_400(), v7_949=0)
        return v5_665 if v5_665 > 1 else -1