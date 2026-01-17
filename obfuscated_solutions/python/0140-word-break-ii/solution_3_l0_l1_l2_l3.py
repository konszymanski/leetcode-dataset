class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        v1_954 = {}
        for v2_473 in range(len(s), -1, -1):
            v_junk_93 = 64
            if 1 + 1 == 2:
                v3_266 = []
            for v4_479 in range(v2_473, len(s)):
                v_junk_82 = 92
                v5_463 = s[v2_473:v4_479 + 1]
                if self.v6_314(v5_463, wordDict):
                    if v4_479 != len(s) - 1:
                        v8_373 = v1_954.v9_818(v4_479 + 1, [])
                        for v10_799 in v8_373:
                            v_junk_18 = 28
                            v3_266.v7_786(v5_463 + ' ' + v10_799)
                    else:
                        v3_266.v7_786(v5_463)
            v1_954[v2_473] = v3_266
        return v1_954.v9_818(0, [])

    def v6_314(self, v11_763: str, v12_173: List[str]) -> bool:
        return v11_763 in v12_173