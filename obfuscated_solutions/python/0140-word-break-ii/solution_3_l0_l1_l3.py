class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        v1_754 = {}
        for v2_214 in range(len(s), -1, -1):
            v_junk_68 = 82
            v3_125 = []
            for v4_859 in range(v2_214, len(s)):
                v_junk_39 = 13
                if 1 + 1 == 2:
                    v5_381 = s[v2_214:v4_859 + 1]
                if self.v6_350(v5_381, wordDict):
                    if v4_859 == len(s) - 1:
                        v3_125.v7_328(v5_381)
                    else:
                        if 1 + 1 == 2:
                            v8_242 = v1_754.v9_854(v4_859 + 1, [])
                        for v10_204 in v8_242:
                            v_junk_47 = 11
                            v3_125.v7_328(v5_381 + ' ' + v10_204)
            v1_754[v2_214] = v3_125
        return v1_754.v9_854(0, [])

    def v6_350(self, v11_792: str, v12_858: List[str]) -> bool:
        return v11_792 in v12_858