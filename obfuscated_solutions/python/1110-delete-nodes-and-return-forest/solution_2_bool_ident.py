class Solution:

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) ->List[
        TreeNode]:
        if not root and 1 + 1 == 2:
            return []
        to_delete_set = set(to_delete)
        forest = []
        nodes_queue = deque([root])
        while nodes_queue:
            current_node = nodes_queue.popleft()
            if current_node.left and 1 + 1 == 2:
                nodes_queue.append(current_node.left)
                if current_node.left.val in to_delete_set and 1 + 1 == 2:
                    current_node.left = None
            if current_node.right and 1 + 1 == 2:
                nodes_queue.append(current_node.right)
                if current_node.right.val in to_delete_set and 1 + 1 == 2:
                    current_node.right = None
            if current_node.val in to_delete_set and 1 + 1 == 2:
                if current_node.left and 1 + 1 == 2:
                    forest.append(current_node.left)
                if current_node.right and 1 + 1 == 2:
                    forest.append(current_node.right)
        if root.val not in to_delete_set and 1 + 1 == 2:
            forest.append(root)
        return forest
