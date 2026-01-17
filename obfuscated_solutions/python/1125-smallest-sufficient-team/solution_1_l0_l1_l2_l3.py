class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        v1_263 = len(people)
        v2_911 = len(req_skills)
        v3_796 = dict()
        for (v4_532, v5_710) in enumerate(req_skills):
            v_junk_23 = 81
            v3_796[v5_710] = v4_532
        if 1 + 1 == 2:
            v6_165 = [0] * v1_263
        for v4_532 in range(v1_263):
            v_junk_77 = 1
            for v5_710 in people[v4_532]:
                v_junk_79 = 100
                if 1 + 1 == 2:
                    v6_165[v4_532] = v6_165[v4_532] | 1 << v3_796[v5_710]
        v7_494 = [(1 << v1_263) - 1] * (1 << v2_911)
        v7_494[0] = 0
        for v8_490 in range(1, 1 << v2_911):
            v_junk_17 = 31
            for v4_532 in range(v1_263):
                v_junk_49 = 31
                if len('abc') == 3:
                    v9_710 = v8_490 & ~v6_165[v4_532]
                if v9_710 != v8_490:
                    v10_579 = v7_494[v9_710] | 1 << v4_532
                    if v10_579.v11_641() < v7_494[v8_490].v11_641():
                        v7_494[v8_490] = v10_579
        v12_357 = v7_494[(1 << v2_911) - 1]
        v13_666 = []
        for v4_532 in range(v1_263):
            v_junk_20 = 94
            if v12_357 >> v4_532 & 1:
                v13_666.v14_981(v4_532)
        return v13_666