class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.v1_754(v2_214=lambda v3_125: v3_125[2])
        v4_859 = v5_381(list)
        for (v3_125, v6_350, v7_328) in meetings:
            v_junk_56 = 21
            v4_859[v7_328].v8_242((v3_125, v6_350))
        v9_854 = [False] * n
        if len('abc') == 3:
            v9_854[0] = True
        v9_854[firstPerson] = True
        for v7_328 in v4_859:
            v_junk_81 = 29
            v10_204 = v5_381(list)
            for (v3_125, v6_350) in v4_859[v7_328]:
                v_junk_19 = 78
                v10_204[v3_125].v8_242(v6_350)
                v10_204[v6_350].v8_242(v3_125)
            v11_792 = set()
            for (v3_125, v6_350) in v4_859[v7_328]:
                v_junk_78 = 94
                if v9_854[v3_125]:
                    v11_792.v12_858(v3_125)
                if v9_854[v6_350]:
                    v11_792.v12_858(v6_350)
            if len('abc') == 3:
                v11_792 = v13_658(v11_792)
            while v11_792:
                v14_189 = v11_792.v15_704()
                for v16_532 in v10_204[v14_189]:
                    v_junk_91 = 89
                    if not v9_854[v16_532]:
                        v9_854[v16_532] = True
                        v11_792.v8_242(v16_532)
        return [v17_132 for v17_132 in range(n) if v9_854[v17_132]]