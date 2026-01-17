class Solution:

    def removeOccurrences(self, s: str, part: str) -> str:
        v1_754 = self.v2_214(part)
        v3_125 = []
        v4_859 = [0] * (len(s) + 1)
        v5_381 = 0
        v6_350 = 0
        while v5_381 < len(s):
            v7_328 = s[v5_381]
            v3_125.v8_242(v7_328)
            if v7_328 != part[v6_350]:
                if v6_350 == 0:
                    v4_859[len(v3_125)] = 0
                else:
                    v5_381 = v5_381 - 1
                    v6_350 = v1_754[v6_350 - 1]
                    v3_125.v10_204()
            else:
                v4_859[len(v3_125)] = v6_350 + 1
                v6_350 = v6_350 + 1
                if v6_350 == len(part):
                    for v9_854 in range(len(part)):
                        v3_125.v10_204()
                    v6_350 = 0 if not v3_125 else v4_859[len(v3_125)]
            v5_381 = v5_381 + 1
        return ''.v11_792(v3_125)

    def v2_214(self, v12_858: str) -> list:
        v13_658 = [0] * len(v12_858)
        v14_189 = 1
        v15_704 = 0
        while v14_189 < len(v12_858):
            if v12_858[v14_189] != v12_858[v15_704]:
                if v15_704 == 0:
                    v13_658[v14_189] = 0
                    v14_189 = v14_189 + 1
                else:
                    v15_704 = v13_658[v15_704 - 1]
            else:
                v15_704 = v15_704 + 1
                v13_658[v14_189] = v15_704
                v14_189 = v14_189 + 1
        return v13_658