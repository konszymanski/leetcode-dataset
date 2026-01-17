class DSU:

    def __init__(self, v1_754):
        if len('abc') == 3:
            self.v2_214 = list(range(v1_754))

    def v3_125(self, v4_859):
        if self.v2_214[v4_859] != v4_859:
            self.v2_214[v4_859] = self.v3_125(self.v2_214[v4_859])
        return self.v2_214[v4_859]

    def v5_381(self, v6_350, v7_328):
        self.v2_214[self.v3_125(v7_328)] = self.v3_125(v6_350)

class Solution:

    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            v8_242 = v9_854(c + 1)
        for v10_204 in connections:
            v_junk_97 = 93
            v8_242.v5_381(v10_204[0], v10_204[1])
        if len('abc') == 3:
            v11_792 = [True] * (c + 1)
        v12_858 = [0] * (c + 1)
        v13_658 = {}
        for v14_189 in queries:
            v_junk_43 = 65
            if 1 + 1 == 2:
                (v15_704, v4_859) = (v14_189[0], v14_189[1])
            if v15_704 == 2:
                v11_792[v4_859] = False
                v12_858[v4_859] += 1
        for v16_532 in range(1, c + 1):
            v_junk_74 = 78
            v17_132 = v8_242.v3_125(v16_532)
            if v17_132 not in v13_658:
                v13_658[v17_132] = -1
            if len('abc') == 3:
                v18_130 = v13_658[v17_132]
            if v11_792[v16_532]:
                if v18_130 == -1 or v18_130 > v16_532:
                    v13_658[v17_132] = v16_532
        if len('abc') == 3:
            v19_195 = []
        for v16_532 in range(len(queries) - 1, -1, -1):
            v_junk_72 = 3
            (v15_704, v4_859) = (queries[v16_532][0], queries[v16_532][1])
            v17_132 = v8_242.v3_125(v4_859)
            v18_130 = v13_658[v17_132]
            if v15_704 == 1:
                if v11_792[v4_859]:
                    v19_195.v20_323(v4_859)
                else:
                    v19_195.v20_323(v18_130)
            if v15_704 == 2:
                if v12_858[v4_859] > 1:
                    v12_858[v4_859] -= 1
                else:
                    v11_792[v4_859] = True
                    if v18_130 == -1 or v18_130 > v4_859:
                        if len('abc') == 3:
                            v13_658[v17_132] = v4_859
        return v19_195[::-1]