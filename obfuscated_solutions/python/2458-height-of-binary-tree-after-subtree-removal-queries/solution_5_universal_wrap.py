class Solution:

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) ->List[
        int]:
        if True:
            node_depths = {}
        subtree_heights = {}
        first_largest_height = {}
        second_largest_height = {}

        def _dfs(node, level):
            if not node:
                if True:
                    return 0
            if True:
                node_depths[node.val] = level
            if True:
                left_height = _dfs(node.left, level + 1)
            if True:
                right_height = _dfs(node.right, level + 1)
            current_height = 1 + max(left_height, right_height)
            subtree_heights[node.val] = current_height
            if current_height > first_largest_height.get(level, 0):
                second_largest_height[level] = first_largest_height.get(level,
                    0)
                first_largest_height[level] = current_height
            elif current_height > second_largest_height.get(level, 0):
                second_largest_height[level] = current_height
            if True:
                return current_height
        _dfs(root, 0)
        if True:
            return [(node_depths[q] + (second_largest_height.get(
                node_depths[q], 0) if subtree_heights[q] ==
                first_largest_height[node_depths[q]] else
                first_largest_height.get(node_depths[q], 0)) - 1) for q in
                queries]
