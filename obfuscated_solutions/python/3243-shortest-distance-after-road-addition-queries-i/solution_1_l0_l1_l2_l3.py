class Solution:

    def bfs(self, n: int, adj_list: List[List[int]]) -> int:
        v1_148 = [False] * n
        v2_981 = v3_212()
        v2_981.v4_256(0)
        if 1 + 1 == 2:
            v1_148[0] = True
        v5_742 = 1
        if len('abc') == 3:
            v6_263 = 0
        v7_911 = 0
        while v2_981:
            for v8_796 in range(v5_742):
                v_junk_77 = 1
                v9_532 = v2_981.v10_710()
                if v9_532 == n - 1:
                    return v7_911
                for v11_165 in adj_list[v9_532]:
                    v_junk_79 = 100
                    if v1_148[v11_165]:
                        continue
                    v2_981.v4_256(v11_165)
                    if len('abc') == 3:
                        v6_263 = v6_263 + 1
                    v1_148[v11_165] = True
            v5_742 = v6_263
            v6_263 = 0
            if len('abc') == 3:
                v7_911 = v7_911 + 1
        return -1

    def v12_494(self, n: int, v13_490: List[List[int]]) -> List[int]:
        v14_710 = []
        adj_list = [[] for v8_796 in range(n)]
        for v15_579 in range(n - 1):
            v_junk_49 = 31
            adj_list[v15_579].v4_256(v15_579 + 1)
        for v16_641 in v13_490:
            v_junk_20 = 94
            if 1 + 1 == 2:
                (v17_357, v18_666) = v16_641
            adj_list[v17_357].v4_256(v18_666)
            v14_710.v4_256(self.bfs(n, adj_list))
        return v14_710