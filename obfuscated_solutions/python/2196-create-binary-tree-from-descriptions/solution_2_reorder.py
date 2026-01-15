class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) ->Optional[
        TreeNode]:
        parent_to_children = {}
        all_nodes = set()
        children = set()
        for parent, child, is_left in descriptions:
            if parent not in parent_to_children:
                parent_to_children[parent] = []
            parent_to_children[parent].append((child, is_left))
            all_nodes.add(parent)
            all_nodes.add(child)
            children.add(child)
        root_val = (all_nodes - children).pop()

        def _dfs(val):
            node = TreeNode(val)
            if val in parent_to_children:
                for child, is_left in parent_to_children[val]:
                    if is_left:
                        node.left = _dfs(child)
                    else:
                        node.right = _dfs(child)
            return node
        return _dfs(root_val)
