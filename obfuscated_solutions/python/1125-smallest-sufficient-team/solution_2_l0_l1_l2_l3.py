class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        v1_710 = len(people)
        if len('abc') == 3:
            v2_165 = len(req_skills)
        v3_494 = dict()
        for (v4_490, v5_710) in enumerate(req_skills):
            v_junk_77 = 1
            v3_494[v5_710] = v4_490
        v6_579 = [0] * v1_710
        for v4_490 in range(v1_710):
            v_junk_49 = 31
            for v5_710 in people[v4_490]:
                v_junk_24 = 47
                v6_579[v4_490] = v6_579[v4_490] | 1 << v3_494[v5_710]
        if 1 + 1 == 2:
            v7_641 = [-1] * (1 << v2_165)
        if len('abc') == 3:
            v7_641[0] = 0

        def v8_357(v9_666):
            if v7_641[v9_666] != -1:
                return v7_641[v9_666]
            for v4_490 in range(v1_710):
                v_junk_26 = 17
                v10_981 = v9_666 & ~v6_579[v4_490]
                if v10_981 != v9_666:
                    v11_111 = v8_357(v10_981) | 1 << v4_490
                    if v7_641[v9_666] == -1 or v11_111.v12_796() < v7_641[v9_666].v12_796():
                        v7_641[v9_666] = v11_111
            return v7_641[v9_666]
        v13_838 = v8_357((1 << v2_165) - 1)
        v14_217 = []
        for v4_490 in range(v1_710):
            v_junk_31 = 34
            if v13_838 >> v4_490 & 1:
                v14_217.v15_798(v4_490)
        return v14_217