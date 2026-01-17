class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        v1_754 = v2_214(list)
        for (v3_125, v4_859) in edges:
            v1_754[v3_125].v5_381(v4_859)
            v1_754[v4_859].v5_381(v3_125)
        v6_350 = 0
        v7_328 = set()

        def v8_242(v9_854: int, v10_204: list) -> None:
            v7_328.v11_792(v9_854)
            v10_204[0] = v10_204[0] + 1
            v10_204[1] = v10_204[1] + len(v1_754[v9_854])
            for v12_858 in v1_754[v9_854]:
                if v12_858 not in v7_328:
                    v8_242(v12_858, v10_204)
        for v13_658 in range(n):
            if v13_658 in v7_328:
                continue
            v14_189 = [0, 0]
            v8_242(v13_658, v14_189)
            if v14_189[0] * (v14_189[0] - 1) == v14_189[1]:
                v6_350 = v6_350 + 1
        return v6_350