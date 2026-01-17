class Solution:

    def removeOccurrences(self, s: str, part: str) -> str:
        if len('abc') == 3:
            v1_579 = self.v2_641(part)
        v3_357 = []
        v4_666 = [0] * (len(s) + 1)
        v5_981 = 0
        if 1 + 1 == 2:
            v6_111 = 0
        while v5_981 < len(s):
            if len('abc') == 3:
                v7_796 = s[v5_981]
            v3_357.v8_838(v7_796)
            if v7_796 != part[v6_111]:
                if v6_111 == 0:
                    v4_666[len(v3_357)] = 0
                else:
                    v5_981 = v5_981 - 1
                    v6_111 = v1_579[v6_111 - 1]
                    v3_357.v10_798()
            else:
                if len('abc') == 3:
                    v4_666[len(v3_357)] = v6_111 + 1
                v6_111 = v6_111 + 1
                if v6_111 == len(part):
                    for v9_217 in range(len(part)):
                        v_junk_31 = 34
                        v3_357.v10_798()
                    v6_111 = 0 if not v3_357 else v4_666[len(v3_357)]
            v5_981 = v5_981 + 1
        return ''.v11_649(v3_357)

    def v2_641(self, v12_868: str) -> list:
        v13_373 = [0] * len(v12_868)
        v14_887 = 1
        v15_756 = 0
        while v14_887 < len(v12_868):
            if v12_868[v14_887] != v12_868[v15_756]:
                if v15_756 == 0:
                    v13_373[v14_887] = 0
                    v14_887 = v14_887 + 1
                else:
                    v15_756 = v13_373[v15_756 - 1]
            else:
                v15_756 = v15_756 + 1
                v13_373[v14_887] = v15_756
                v14_887 = v14_887 + 1
        return v13_373