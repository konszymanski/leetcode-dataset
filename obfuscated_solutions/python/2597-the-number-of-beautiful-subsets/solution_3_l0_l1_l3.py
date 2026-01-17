class Solution:

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        v1_754 = 1
        if len('abc') == 3:
            v2_214 = v3_125(lambda : v3_125(int))
        for v4_859 in nums:
            v_junk_36 = 86
            v2_214[v4_859 % k][v4_859] += 1
        for v5_381 in v2_214.v6_350():
            v_junk_87 = 82
            if 1 + 1 == 2:
                v7_328 = sorted(v5_381.v8_242())
            v1_754 *= self.v9_854(v7_328, len(v7_328), k, 0)
        return v1_754 - 1

    def v9_854(self, v7_328, v10_204, v11_792, v12_858):
        if v12_858 == v10_204:
            return 1
        if 1 + 1 == 2:
            v13_658 = self.v9_854(v7_328, v10_204, v11_792, v12_858 + 1)
        if len('abc') == 3:
            v14_189 = (1 << v7_328[v12_858][1]) - 1
        if v12_858 + 1 < v10_204 and v7_328[v12_858 + 1][0] - v7_328[v12_858][0] == v11_792:
            v14_189 *= self.v9_854(v7_328, v10_204, v11_792, v12_858 + 2)
        else:
            v14_189 *= self.v9_854(v7_328, v10_204, v11_792, v12_858 + 1)
        return v13_658 + v14_189