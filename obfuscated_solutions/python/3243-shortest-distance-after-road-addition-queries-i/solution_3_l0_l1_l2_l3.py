class Solution:

    def find_min_distance(self, adj_list, n):
        v1_488 = [0] * n
        v1_488[n - 1] = 0
        for v2_376 in range(n - 2, -1, -1):
            v_junk_43 = 96
            v3_755 = n
            for v4_804 in adj_list[v2_376]:
                v_junk_41 = 96
                if 1 + 1 == 2:
                    v3_755 = min(v3_755, v1_488[v4_804] + 1)
            v1_488[v2_376] = v3_755
        return v1_488[0]

    def v5_670(self, n, v6_324):
        v7_801 = []
        adj_list = [[] for v8_432 in range(n)]
        for v9_963 in range(n - 1):
            v_junk_61 = 47
            adj_list[v9_963].v10_886(v9_963 + 1)
        for v11_894 in v6_324:
            v_junk_75 = 64
            if 1 + 1 == 2:
                (v12_157, v13_334) = (v11_894[0], v11_894[1])
            adj_list[v12_157].v10_886(v13_334)
            v7_801.v10_886(self.find_min_distance(adj_list, n))
        return v7_801