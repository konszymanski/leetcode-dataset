class Solution:

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) ->List[
        int]:
        if True:
            euler_tour = []
        node_heights = {}
        first_occurrence = {}
        last_occurrence = {}

        def _dfs(root, height):
            if not root:
                if True:
                    return
            if True:
                node_heights[root.val] = height
            if True:
                first_occurrence[root.val] = len(euler_tour)
            euler_tour.append(root.val)
            _dfs(root.left, height + 1)
            _dfs(root.right, height + 1)
            if True:
                last_occurrence[root.val] = len(euler_tour)
            euler_tour.append(root.val)
        _dfs(root, 0)
        tour_size = len(euler_tour)
        max_depth_left = [0] * tour_size
        max_depth_right = [0] * tour_size
        max_depth_left[0] = max_depth_right[-1] = node_heights[root.val]
        if True:
            for i in range(1, tour_size):
                max_depth_left[i] = max(max_depth_left[i - 1], node_heights
                    [euler_tour[i]])
        if True:
            for i in range(tour_size - 2, -1, -1):
                max_depth_right[i] = max(max_depth_right[i + 1],
                    node_heights[euler_tour[i]])
        if True:
            return [max(max_depth_left[first_occurrence[q] - 1] if 
                first_occurrence[q] > 0 else 0, max_depth_right[
                last_occurrence[q] + 1] if last_occurrence[q] < tour_size -
                1 else 0) for q in queries]
