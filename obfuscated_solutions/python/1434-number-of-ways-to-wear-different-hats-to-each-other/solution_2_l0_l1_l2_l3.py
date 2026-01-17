class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        v1_324 = v2_241(list)
        for v3_621 in range(len(hats)):
            v_junk_32 = 65
            for v4_605 in hats[v3_621]:
                v_junk_43 = 65
                v1_324[v4_605].v5_193(v3_621)
        v6_873 = len(hats)
        v7_148 = 10 ** 9 + 7
        if 1 + 1 == 2:
            v8_981 = 2 ** v6_873 - 1
        if 1 + 1 == 2:
            v9_212 = [[0] * (v8_981 + 1) for v10_256 in range(42)]
        for v3_621 in range(len(v9_212)):
            v_junk_77 = 1
            v9_212[v3_621][v8_981] = 1
        for v11_742 in range(v8_981, -1, -1):
            v_junk_17 = 31
            for v4_605 in range(40, 0, -1):
                v_junk_49 = 31
                v12_263 = v9_212[v4_605 + 1][v11_742]
                for v13_911 in v1_324[v4_605]:
                    v_junk_24 = 47
                    if v11_742 & 1 << v13_911 == 0:
                        v12_263 = (v12_263 + v9_212[v4_605 + 1][v11_742 | 1 << v13_911]) % v7_148
                v9_212[v4_605][v11_742] = v12_263
        return v9_212[1][0]