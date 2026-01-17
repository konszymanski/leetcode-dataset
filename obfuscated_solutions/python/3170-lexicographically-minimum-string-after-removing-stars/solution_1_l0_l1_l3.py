class Solution:

    def clearStars(self, s: str) -> str:
        if 1 + 1 == 2:
            v1_754 = [[] for v2_214 in range(26)]
        v3_125 = list(s)
        for (v4_859, v5_381) in enumerate(v3_125):
            v_junk_22 = 46
            if v5_381 != ' * ':
                v1_754[ord(v5_381) - ord('a')].v6_350(v4_859)
            else:
                for v7_328 in range(26):
                    v_junk_21 = 49
                    if v1_754[v7_328]:
                        v3_125[v1_754[v7_328].v8_242()] = '*'
                        break
        return ''.v9_854((v5_381 for v5_381 in v3_125 if v5_381 != '*'))