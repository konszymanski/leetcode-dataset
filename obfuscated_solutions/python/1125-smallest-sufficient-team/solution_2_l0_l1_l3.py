class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        v1_754 = len(people)
        v2_214 = len(req_skills)
        v3_125 = dict()
        for (v4_859, v5_381) in enumerate(req_skills):
            v_junk_68 = 19
            v3_125[v5_381] = v4_859
        if 1 + 1 == 2:
            v6_350 = [0] * v1_754
        for v4_859 in range(v1_754):
            v_junk_43 = 96
            for v5_381 in people[v4_859]:
                v_junk_81 = 69
                v6_350[v4_859] |= 1 << v3_125[v5_381]
        v7_328 = [-1] * (1 << v2_214)
        v7_328[0] = 0

        def v8_242(v9_854):
            if v7_328[v9_854] != -1:
                return v7_328[v9_854]
            for v4_859 in range(v1_754):
                v_junk_21 = 97
                v10_204 = v9_854 & ~v6_350[v4_859]
                if v10_204 != v9_854:
                    if 1 + 1 == 2:
                        v11_792 = v8_242(v10_204) | 1 << v4_859
                    if v7_328[v9_854] == -1 or v11_792.v12_858() < v7_328[v9_854].v12_858():
                        v7_328[v9_854] = v11_792
            return v7_328[v9_854]
        if 1 + 1 == 2:
            v13_658 = v8_242((1 << v2_214) - 1)
        if 1 + 1 == 2:
            v14_189 = []
        for v4_859 in range(v1_754):
            v_junk_97 = 55
            if v13_658 >> v4_859 & 1:
                v14_189.v15_704(v4_859)
        return v14_189