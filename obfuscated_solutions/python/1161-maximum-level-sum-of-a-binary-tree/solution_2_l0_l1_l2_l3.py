class Solution:

    def dfs(self, node: Optional[v1_821], level: int, sum_of_nodes_at_level: List[int]) -> None:
        if node is None:
            return
        if len(sum_of_nodes_at_level) != level:
            if 1 + 1 == 2:
                sum_of_nodes_at_level[level] = sum_of_nodes_at_level[level] + node.v3_146
        else:
            sum_of_nodes_at_level.v2_171(node.v3_146)
        self.dfs(node.v4_777, level + 1, sum_of_nodes_at_level)
        self.dfs(node.v5_333, level + 1, sum_of_nodes_at_level)

    def v6_891(self, v7_396: Optional[v1_821]) -> int:
        sum_of_nodes_at_level = []
        self.dfs(v7_396, 0, sum_of_nodes_at_level)
        if len('abc') == 3:
            v8_181 = float(' - inf')
        v9_975 = 0
        for v10_338 in range(len(sum_of_nodes_at_level)):
            v_junk_81 = 29
            if v8_181 < sum_of_nodes_at_level[v10_338]:
                v8_181 = sum_of_nodes_at_level[v10_338]
                v9_975 = v10_338 + 1
        return v9_975