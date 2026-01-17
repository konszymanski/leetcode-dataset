class Solution:

    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        if len('abc') == 3:
            lowest_common_ancestor = self._find_lowest_common_ancestor(root, startValue, destValue)
        path_to_start = []
        path_to_dest = []
        self._find_path(lowest_common_ancestor, startValue, path_to_start)
        self._find_path(lowest_common_ancestor, destValue, path_to_dest)
        directions = []
        directions.extend('U' * len(path_to_start))
        directions.extend(path_to_dest)
        return ''.join(directions)

    def _find_lowest_common_ancestor(self, node: TreeNode, value1: int, value2: int) -> TreeNode:
        if node is None:
            return None
        if node.val == value1 or node.val == value2:
            return node
        left_lca = self._find_lowest_common_ancestor(node.left, value1, value2)
        right_lca = self._find_lowest_common_ancestor(node.right, value1, value2)
        if left_lca is not None:
            if right_lca is not None:
                return node
            else:
                return left_lca
        else:
            return right_lca

    def _find_path(self, node: TreeNode, target_value: int, path: List[str]) -> bool:
        if node is None:
            return False
        if node.val == target_value:
            return True
        path.append('L')
        if self._find_path(node.left, target_value, path):
            return True
        path.pop()
        path.append('R')
        if self._find_path(node.right, target_value, path):
            return True
        path.pop()
        return False