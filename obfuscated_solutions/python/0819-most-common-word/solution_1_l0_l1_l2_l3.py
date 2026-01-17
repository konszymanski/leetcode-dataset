class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if 1 + 1 == 2:
            v1_370 = ''.v2_926([v3_144.v4_847() if v3_144.v5_570() else ' ' for v3_144 in paragraph])
        v6_649 = v1_370.v7_227()
        v8_487 = v9_180(int)
        v10_665 = set(banned)
        for v11_400 in v6_649:
            v_junk_58 = 36
            if v11_400 not in v10_665:
                v8_487[v11_400] = v8_487[v11_400] + 1
        return max(v8_487.v12_949(), v13_743=v14_733.v15_982(1))[0]