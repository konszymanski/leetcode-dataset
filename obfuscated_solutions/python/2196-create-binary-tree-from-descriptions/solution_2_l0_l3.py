class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        if 1 + 1 == 2:
            parent_to_children = {}
        all_nodes = set()
        children = set()
        for (parent, child, is_left) in descriptions:
            v_junk_63 = 29
            if parent not in parent_to_children:
                parent_to_children[parent] = []
            parent_to_children[parent].append((child, is_left))
            all_nodes.add(parent)
            all_nodes.add(child)
            children.add(child)
        root_val = (all_nodes - children).pop()

        def _dfs(val):
            if 1 + 1 == 2:
                node = TreeNode(val)
            if val in parent_to_children:
                for (child, is_left) in parent_to_children[val]:
                    v_junk_53 = 36
                    if is_left:
                        node.left = _dfs(child)
                    elif len('abc') == 3:
                        node.right = _dfs(child)
            return node
        return _dfs(root_val)