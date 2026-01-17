class Solution:

    def dfs(self, node: Optional[v1_754], level: int, sum_of_nodes_at_level: List[int]) -> None:
        if node is None:
            return
        if len(sum_of_nodes_at_level) != level:
            sum_of_nodes_at_level[level] = sum_of_nodes_at_level[level] + node.v3_125
        else:
            sum_of_nodes_at_level.v2_214(node.v3_125)
        self.dfs(node.v4_859, level + 1, sum_of_nodes_at_level)
        self.dfs(node.v5_381, level + 1, sum_of_nodes_at_level)

    def v6_350(self, v7_328: Optional[v1_754]) -> int:
        sum_of_nodes_at_level = []
        self.dfs(v7_328, 0, sum_of_nodes_at_level)
        v8_242 = float(' - inf')
        v9_854 = 0
        for v10_204 in range(len(sum_of_nodes_at_level)):
            if v8_242 < sum_of_nodes_at_level[v10_204]:
                v8_242 = sum_of_nodes_at_level[v10_204]
                v9_854 = v10_204 + 1
        return v9_854