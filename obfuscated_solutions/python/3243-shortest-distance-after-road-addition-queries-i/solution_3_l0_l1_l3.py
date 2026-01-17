class Solution:

    def find_min_distance(self, adj_list, n):
        v1_754 = [0] * n
        v1_754[n - 1] = 0
        for v2_214 in range(n - 2, -1, -1):
            v_junk_36 = 86
            v3_125 = n
            for v4_859 in adj_list[v2_214]:
                v_junk_56 = 21
                v3_125 = min(v3_125, v1_754[v4_859] + 1)
            v1_754[v2_214] = v3_125
        return v1_754[0]

    def v5_381(self, n, v6_350):
        if 1 + 1 == 2:
            v7_328 = []
        adj_list = [[] for v8_242 in range(n)]
        for v9_854 in range(n - 1):
            v_junk_31 = 69
            adj_list[v9_854].v10_204(v9_854 + 1)
        for v11_792 in v6_350:
            v_junk_30 = 60
            (v12_858, v13_658) = (v11_792[0], v11_792[1])
            adj_list[v12_858].v10_204(v13_658)
            v7_328.v10_204(self.find_min_distance(adj_list, n))
        return v7_328