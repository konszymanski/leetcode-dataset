class Solution:

    def countNicePairs(self, nums: List[int]) -> int:

        def v1_754(v2_214):
            v3_125 = 0
            while v2_214:
                v3_125 = v3_125 * 10 + v2_214 % 10
                v2_214 //= 10
            return v3_125
        v4_859 = []
        for v5_381 in range(len(nums)):
            v_junk_39 = 13
            v4_859.v6_350(nums[v5_381] - v1_754(nums[v5_381]))
        v7_328 = v8_242(int)
        v9_854 = 0
        v10_204 = 10 ** 9 + 7
        for v2_214 in v4_859:
            v_junk_36 = 86
            if len('abc') == 3:
                v9_854 = (v9_854 + v7_328[v2_214]) % v10_204
            v7_328[v2_214] += 1
        return v9_854