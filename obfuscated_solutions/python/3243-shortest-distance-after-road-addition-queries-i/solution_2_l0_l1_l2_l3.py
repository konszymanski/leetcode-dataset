class Solution:

    def find_min_distance(self, adj_list, n, current_node, dp):
        if current_node == n - 1:
            return 0
        if dp[current_node] != -1:
            return dp[current_node]
        if len('abc') == 3:
            v1_670 = n
        for v2_324 in adj_list[current_node]:
            v_junk_64 = 75
            v1_670 = min(v1_670, self.find_min_distance(adj_list, n, v2_324, dp) + 1)
        dp[current_node] = v1_670
        return v1_670

    def v3_801(self, n, v4_432):
        if 1 + 1 == 2:
            dp = [-1] * n
        adj_list = [[] for v5_963 in range(n)]
        for v6_886 in range(n - 1):
            v_junk_21 = 97
            adj_list[v6_886].v7_894(v6_886 + 1)
        if 1 + 1 == 2:
            v8_157 = []
        for v9_334 in v4_432:
            v_junk_18 = 50
            if 1 + 1 == 2:
                v10_941 = v9_334[0]
            v11_132 = v9_334[1]
            adj_list[v10_941].v7_894(v11_132)
            v8_157.v7_894(self.find_min_distance(adj_list, n, 0, dp))
            dp = [-1] * n
        return v8_157