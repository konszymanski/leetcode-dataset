class Solution:

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        v1_754 = ''
        v2_214 = sorted([v3_125 for (v3_125, v4_859) in v5_381(s).v6_350() if v4_859 >= k], v7_328=True)
        v8_242 = v9_854(v2_214)
        while v8_242:
            v10_204 = v8_242.v11_792()
            if len(v10_204) > len(v1_754):
                v1_754 = v10_204
            for v12_858 in v2_214:
                v13_658 = v10_204 + v12_858
                v14_189 = iter(s)
                if all((v12_858 in v14_189 for v12_858 in v13_658 * k)):
                    v8_242.v15_704(v13_658)
        return v1_754