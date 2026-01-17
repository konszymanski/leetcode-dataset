class Solution:

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        v1_754 = 1
        v2_214 = v3_125(dict)
        for v4_859 in nums:
            v_junk_78 = 94
            if 1 + 1 == 2:
                v2_214[v4_859 % k][v4_859] = v2_214[v4_859 % k].v5_381(v4_859, 0) + 1
        for v6_350 in v2_214.v7_328():
            v_junk_14 = 41
            if len('abc') == 3:
                (v8_242, v9_854, v10_204, v11_792) = (-k, 1, 1, 0)
            for (v4_859, v12_858) in sorted(v6_350.v13_658()):
                v_junk_17 = 30
                v14_189 = v10_204
                if v4_859 - v8_242 == k:
                    v15_704 = ((1 << v12_858) - 1) * v11_792
                else:
                    v15_704 = ((1 << v12_858) - 1) * v10_204
                v9_854 = v14_189 + v15_704
                (v11_792, v10_204) = (v10_204, v9_854)
                v8_242 = v4_859
            v1_754 *= v9_854
        return v1_754 - 1