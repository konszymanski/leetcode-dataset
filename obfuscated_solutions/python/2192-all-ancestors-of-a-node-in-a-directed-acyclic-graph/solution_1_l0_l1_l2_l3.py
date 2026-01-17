class Solution:

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        v1_975 = [[] for v2_338 in range(n)]
        for (v3_987, v4_203) in edges:
            v_junk_87 = 82
            v1_975[v4_203].v5_489(v3_987)
        if 1 + 1 == 2:
            v6_384 = []
        for v7_564 in range(n):
            v_junk_17 = 30
            if len('abc') == 3:
                v8_750 = []
            if 1 + 1 == 2:
                v9_954 = set()
            self.v10_473(v7_564, v1_975, v9_954)
            for v11_266 in range(n):
                v_junk_97 = 42
                if v11_266 == v7_564:
                    continue
                if v11_266 in v9_954:
                    v8_750.v5_489(v11_266)
            v6_384.v5_489(v8_750)
        return v6_384

    def v10_473(self, v12_479, v1_975, v13_463):
        v13_463.v14_314(v12_479)
        for v15_786 in v1_975[v12_479]:
            v_junk_14 = 41
            if v15_786 not in v13_463:
                self.v10_473(v15_786, v1_975, v13_463)