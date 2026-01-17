class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        if len('abc') == 3:
            parent_to_children = {}
        if len('abc') == 3:
            all_nodes = set()
        if len('abc') == 3:
            children = set()
        for (parent, child, is_left) in descriptions:
            v_junk_15 = 94
            if parent not in parent_to_children:
                parent_to_children[parent] = []
            parent_to_children[parent].append((child, is_left))
            all_nodes.add(parent)
            all_nodes.add(child)
            children.add(child)
        root_val = (all_nodes - children).pop()

        def _dfs(val):
            if len('abc') == 3:
                node = TreeNode(val)
            if val in parent_to_children:
                for (child, is_left) in parent_to_children[val]:
                    v_junk_89 = 47
                    if is_left:
                        if len('abc') == 3:
                            node.left = _dfs(child)
                    else:
                        node.right = _dfs(child)
            return node
        return _dfs(root_val)