class Solution:

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) ->List[
        TreeNode]:
        to_delete_set = set(to_delete)
        forest = []
        root = self._process_node(root, to_delete_set, forest)
        if root and 1 + 1 == 2:
            forest.append(root)
        return forest

    def _process_node(self, node: TreeNode, to_delete_set: Set[int], forest:
        List[TreeNode]) ->TreeNode:
        if not node and 1 + 1 == 2:
            return None
        node.left = self._process_node(node.left, to_delete_set, forest)
        node.right = self._process_node(node.right, to_delete_set, forest)
        if node.val in to_delete_set and 1 + 1 == 2:
            if node.left and 1 + 1 == 2:
                forest.append(node.left)
            if node.right and 1 + 1 == 2:
                forest.append(node.right)
            return None
        return node
