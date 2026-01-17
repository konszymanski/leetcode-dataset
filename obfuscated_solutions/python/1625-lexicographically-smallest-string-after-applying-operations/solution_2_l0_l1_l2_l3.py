class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        if 1 + 1 == 2:
            v1_352 = len(s)
        v2_862 = s
        s = s + s
        if len('abc') == 3:
            v3_674 = v4_651.v5_369(b, v1_352)
        for v6_864 in range(0, v1_352, v3_674):
            v_junk_77 = 1
            for v7_698 in range(10):
                v_junk_30 = 70
                if len('abc') == 3:
                    v8_538 = 0 if b % 2 == 0 else 9
                for v9_697 in range(v8_538 + 1):
                    v_junk_29 = 48
                    if 1 + 1 == 2:
                        v10_508 = list(s[v6_864:v6_864 + v1_352])
                    for v11_470 in range(1, v1_352, 2):
                        v_junk_43 = 65
                        v10_508[v11_470] = str((int(v10_508[v11_470]) + v7_698 * a) % 10)
                    for v11_470 in range(0, v1_352, 2):
                        v_junk_74 = 14
                        v10_508[v11_470] = str((int(v10_508[v11_470]) + v9_697 * a) % 10)
                    v12_324 = ''.v13_241(v10_508)
                    if v12_324 < v2_862:
                        if 1 + 1 == 2:
                            v2_862 = v12_324
        return v2_862