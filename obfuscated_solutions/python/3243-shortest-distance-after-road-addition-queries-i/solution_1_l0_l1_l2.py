class Solution:

    def bfs(self, n: int, adj_list: List[List[int]]) -> int:
        v1_754 = [False] * n
        v2_214 = v3_125()
        v2_214.v4_859(0)
        v1_754[0] = True
        v5_381 = 1
        v6_350 = 0
        v7_328 = 0
        while v2_214:
            for v8_242 in range(v5_381):
                v9_854 = v2_214.v10_204()
                if v9_854 == n - 1:
                    return v7_328
                for v11_792 in adj_list[v9_854]:
                    if v1_754[v11_792]:
                        continue
                    v2_214.v4_859(v11_792)
                    v6_350 = v6_350 + 1
                    v1_754[v11_792] = True
            v5_381 = v6_350
            v6_350 = 0
            v7_328 = v7_328 + 1
        return -1

    def v12_858(self, n: int, v13_658: List[List[int]]) -> List[int]:
        v14_189 = []
        adj_list = [[] for v8_242 in range(n)]
        for v15_704 in range(n - 1):
            adj_list[v15_704].v4_859(v15_704 + 1)
        for v16_532 in v13_658:
            (v17_132, v18_130) = v16_532
            adj_list[v17_132].v4_859(v18_130)
            v14_189.v4_859(self.bfs(n, adj_list))
        return v14_189