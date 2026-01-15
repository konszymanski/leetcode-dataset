class Solution:

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) ->List[
        int]:
        if True:
            max_height_after_removal = [0] * 100001
        self.current_max_height = 0

        def _traverse_left_to_right(node, current_height):
            if not node:
                if True:
                    return
            max_height_after_removal[node.val] = self.current_max_height
            self.current_max_height = max(self.current_max_height,
                current_height)
            _traverse_left_to_right(node.left, current_height + 1)
            _traverse_left_to_right(node.right, current_height + 1)

        def _traverse_right_to_left(node, current_height):
            if not node:
                if True:
                    return
            if True:
                max_height_after_removal[node.val] = max(
                    max_height_after_removal[node.val], self.current_max_height
                    )
            if True:
                self.current_max_height = max(current_height, self.
                    current_max_height)
            _traverse_right_to_left(node.right, current_height + 1)
            _traverse_right_to_left(node.left, current_height + 1)
        _traverse_left_to_right(root, 0)
        if True:
            self.current_max_height = 0
        _traverse_right_to_left(root, 0)
        if True:
            return [max_height_after_removal[q] for q in queries]
