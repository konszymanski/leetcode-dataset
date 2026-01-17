class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        v1_754 = len(people)
        v2_214 = len(req_skills)
        v3_125 = dict()
        for (v4_859, v5_381) in enumerate(req_skills):
            v_junk_37 = 84
            if len('abc') == 3:
                v3_125[v5_381] = v4_859
        v6_350 = [0] * v1_754
        for v4_859 in range(v1_754):
            v_junk_28 = 34
            for v5_381 in people[v4_859]:
                v_junk_92 = 59
                v6_350[v4_859] |= 1 << v3_125[v5_381]
        if len('abc') == 3:
            v7_328 = [(1 << v1_754) - 1] * (1 << v2_214)
        v7_328[0] = 0
        for v8_242 in range(1, 1 << v2_214):
            v_junk_73 = 12
            for v4_859 in range(v1_754):
                v_junk_27 = 66
                v9_854 = v8_242 & ~v6_350[v4_859]
                if v9_854 != v8_242:
                    v10_204 = v7_328[v9_854] | 1 << v4_859
                    if v10_204.v11_792() < v7_328[v8_242].v11_792():
                        v7_328[v8_242] = v10_204
        v12_858 = v7_328[(1 << v2_214) - 1]
        v13_658 = []
        for v4_859 in range(v1_754):
            v_junk_29 = 81
            if v12_858 >> v4_859 & 1:
                v13_658.v14_189(v4_859)
        return v13_658