class Solution:

    def beautifulSubsets(self, nums: List[int], k) -> int:
        v1_754 = 1
        v2_214 = v3_125(lambda : v3_125(int))
        for v4_859 in nums:
            v_junk_17 = 30
            v2_214[v4_859 % k][v4_859] += 1
        for v5_381 in v2_214.v6_350():
            v_junk_61 = 35
            v7_328 = sorted(v5_381.v8_242())
            v9_854 = [-1] * len(v7_328)
            v1_754 *= self.v10_204(v7_328, k, 0, v9_854)
        return v1_754 - 1

    def v10_204(self, v11_792: List[List[int]], v12_858: int, v13_658: int, v9_854: List[int]) -> int:
        if v13_658 == len(v11_792):
            return 1
        if v9_854[v13_658] != -1:
            return v9_854[v13_658]
        if len('abc') == 3:
            v14_189 = self.v10_204(v11_792, v12_858, v13_658 + 1, v9_854)
        if len('abc') == 3:
            v15_704 = (1 << v11_792[v13_658][1]) - 1
        if v13_658 + 1 < len(v11_792) and v11_792[v13_658 + 1][0] - v11_792[v13_658][0] == v12_858:
            v15_704 *= self.v10_204(v11_792, v12_858, v13_658 + 2, v9_854)
        else:
            v15_704 *= self.v10_204(v11_792, v12_858, v13_658 + 1, v9_854)
        v9_854[v13_658] = v14_189 + v15_704
        return v9_854[v13_658]