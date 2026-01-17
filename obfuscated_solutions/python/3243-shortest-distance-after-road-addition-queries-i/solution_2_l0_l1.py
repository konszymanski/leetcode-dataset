class Solution:
    def find_min_distance(self, adj_list, n, current_node, dp):
        if current_node  ==  n  -  1:
            return 0
        if dp[current_node]  !=  -1:
            return dp[current_node]
        v1_754 = n
        for v2_214 in adj_list[current_node]:
            v1_754 = min(
                v1_754,
                self.find_min_distance(adj_list, n, v2_214, dp) + 1,
            )
        dp[current_node] = v1_754
        return v1_754
    def v3_125(self, n, v4_859):
        dp = [-1]  *  n
        adj_list = [[] for v5_381 in range(n)]
        for v6_350 in range(n  -  1):
            adj_list[v6_350].v7_328(v6_350  +  1)
        v8_242 = []
        for v9_854 in v4_859:
            v10_204 = v9_854[0]
            v11_792 = v9_854[1]
            adj_list[v10_204].v7_328(v11_792)
            v8_242.v7_328(self.find_min_distance(adj_list, n, 0, dp))
            dp = [ - 1] * n
        return v8_242
