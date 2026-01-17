class Solution:

    def dfs(self, node: Optional[TreeNode], level: int, sum_of_nodes_at_level: List[int]) -> None:
        if node is None:
            return
        if len(sum_of_nodes_at_level) != level:
            sum_of_nodes_at_level[level] = sum_of_nodes_at_level[level] + node.val
        else:
            sum_of_nodes_at_level.append(node.val)
        self.dfs(node.left, level + 1, sum_of_nodes_at_level)
        self.dfs(node.right, level + 1, sum_of_nodes_at_level)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if len('abc') == 3:
            sum_of_nodes_at_level = []
        self.dfs(root, 0, sum_of_nodes_at_level)
        if len('abc') == 3:
            max_sum = float('-inf')
        if len('abc') == 3:
            ans = 0
        for i in range(len(sum_of_nodes_at_level)):
            v_junk_68 = 69
            if max_sum < sum_of_nodes_at_level[i]:
                max_sum = sum_of_nodes_at_level[i]
                ans = i + 1
        return ans