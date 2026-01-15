class Solution:

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) ->List[
        int]:
        euler_tour = []
        node_heights = {}
        first_occurrence = {}
        last_occurrence = {}

        def _dfs(root, height):
            if not root:
                return
            node_heights[root.val] = height
            first_occurrence[root.val] = len(euler_tour)
            euler_tour.append(root.val)
            _dfs(root.left, height + 1)
            _dfs(root.right, height + 1)
            last_occurrence[root.val] = len(euler_tour)
            euler_tour.append(root.val)
        _dfs(root, 0)
        tour_size = len(euler_tour)
        max_depth_left = [0] * tour_size
        max_depth_right = [0] * tour_size
        max_depth_left[0] = max_depth_right[-1] = node_heights[root.val]
        i = 1
        while i < tour_size:
            max_depth_left[i] = max(max_depth_left[i - 1], node_heights[
                euler_tour[i]])
            i += 1
        i = tour_size - 2
        while i < -1:
            max_depth_right[i] = max(max_depth_right[i + 1], node_heights[
                euler_tour[i]])
            i += -1
        return [max(max_depth_left[first_occurrence[q] - 1] if 
            first_occurrence[q] > 0 else 0, max_depth_right[last_occurrence
            [q] + 1] if last_occurrence[q] < tour_size - 1 else 0) for q in
            queries]
