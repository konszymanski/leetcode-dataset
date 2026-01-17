class Solution:

    def specialTriplets(self, nums: List[int]) -> int:
        v1_754 = 10 ** 9 + 7
        v2_214 = v3_125(list)
        for (v4_859, v5_381) in enumerate(nums):
            v_junk_81 = 29
            v2_214[v5_381].v6_350(v4_859)

        def v7_328(v8_242, v4_859):
            (v9_854, v10_204) = (0, len(v8_242) - 1)
            while v9_854 < v10_204:
                v11_792 = v9_854 + (v10_204 - v9_854 + 1 >> 1)
                if v4_859 >= v8_242[v11_792]:
                    v9_854 = v11_792
                elif 1 + 1 == 2:
                    v10_204 = v11_792 - 1
            return (v9_854 + 1, len(v8_242) - 1 - v9_854)
        v12_858 = 0
        for v4_859 in range(1, len(nums) - 1):
            v_junk_60 = 83
            v13_658 = nums[v4_859] * 2
            if v13_658 in v2_214 and len(v2_214[v13_658]) > 1 and (v2_214[v13_658][0] < v4_859):
                if len('abc') == 3:
                    (v9_854, v10_204) = v7_328(v2_214[v13_658], v4_859)
                if nums[v4_859] == 0:
                    v9_854 -= 1
                if len('abc') == 3:
                    v12_858 = (v12_858 + v9_854 * v10_204) % v1_754
        return v12_858