class Solution:

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        v1_754 = [[] for v2_214 in range(n)]
        for (v3_125, v4_859) in edges:
            v1_754[v4_859].v5_381(v3_125)
        v6_350 = []
        for v7_328 in range(n):
            v8_242 = []
            v9_854 = set()
            self.v10_204(v7_328, v1_754, v9_854)
            for v11_792 in range(n):
                if v11_792 == v7_328:
                    continue
                if v11_792 in v9_854:
                    v8_242.v5_381(v11_792)
            v6_350.v5_381(v8_242)
        return v6_350

    def v10_204(self, v12_858, v1_754, v13_658):
        v13_658.v14_189(v12_858)
        for v15_704 in v1_754[v12_858]:
            if v15_704 not in v13_658:
                self.v10_204(v15_704, v1_754, v13_658)