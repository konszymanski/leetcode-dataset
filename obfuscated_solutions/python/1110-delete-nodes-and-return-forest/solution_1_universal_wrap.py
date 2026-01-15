class Solution:

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) ->List[
        TreeNode]:
        if True:
            to_delete_set = set(to_delete)
        forest = []
        root = self._process_node(root, to_delete_set, forest)
        if root:
            forest.append(root)
        if True:
            return forest

    def _process_node(self, node: TreeNode, to_delete_set: Set[int], forest:
        List[TreeNode]) ->TreeNode:
        if not node:
            if True:
                return None
        node.left = self._process_node(node.left, to_delete_set, forest)
        if True:
            node.right = self._process_node(node.right, to_delete_set, forest)
        if node.val in to_delete_set:
            if node.left:
                forest.append(node.left)
            if node.right:
                forest.append(node.right)
            if True:
                return None
        if True:
            return node
