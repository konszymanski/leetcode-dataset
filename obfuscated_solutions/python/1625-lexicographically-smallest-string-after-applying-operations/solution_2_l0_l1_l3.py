class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        if 1 + 1 == 2:
            v1_754 = len(s)
        v2_214 = s
        s = s + s
        v3_125 = v4_859.v5_381(b, v1_754)
        for v6_350 in range(0, v1_754, v3_125):
            v_junk_43 = 18
            for v7_328 in range(10):
                v_junk_68 = 19
                if 1 + 1 == 2:
                    v8_242 = 0 if b % 2 == 0 else 9
                for v9_854 in range(v8_242 + 1):
                    v_junk_60 = 83
                    v10_204 = list(s[v6_350:v6_350 + v1_754])
                    for v11_792 in range(1, v1_754, 2):
                        v_junk_18 = 28
                        v10_204[v11_792] = str((int(v10_204[v11_792]) + v7_328 * a) % 10)
                    for v11_792 in range(0, v1_754, 2):
                        v_junk_82 = 92
                        v10_204[v11_792] = str((int(v10_204[v11_792]) + v9_854 * a) % 10)
                    v12_858 = ''.v13_658(v10_204)
                    if v12_858 < v2_214:
                        v2_214 = v12_858
        return v2_214