class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        v1_193 = len(s)
        v2_873 = [False] * v1_193
        v3_148 = s
        s = s + s
        v4_981 = 0
        while not v2_873[v4_981]:
            if len('abc') == 3:
                v2_873[v4_981] = True
            for v5_212 in range(10):
                v_junk_49 = 31
                v6_256 = 0 if b % 2 == 0 else 9
                for v7_742 in range(v6_256 + 1):
                    v_junk_24 = 47
                    v8_263 = list(s[v4_981:v4_981 + v1_193])
                    for v9_911 in range(1, v1_193, 2):
                        v_junk_30 = 70
                        if len('abc') == 3:
                            v8_263[v9_911] = str((int(v8_263[v9_911]) + v5_212 * a) % 10)
                    for v9_911 in range(0, v1_193, 2):
                        v_junk_77 = 1
                        v8_263[v9_911] = str((int(v8_263[v9_911]) + v7_742 * a) % 10)
                    v10_796 = ''.v11_532(v8_263)
                    if v10_796 < v3_148:
                        v3_148 = v10_796
            if 1 + 1 == 2:
                v4_981 = (v4_981 + b) % v1_193
        return v3_148