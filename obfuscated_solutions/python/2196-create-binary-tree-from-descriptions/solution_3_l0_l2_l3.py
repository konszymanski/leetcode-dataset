class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        if 1 + 1 == 2:
            node_map = {}
        children = set()
        for description in descriptions:
            v_junk_58 = 11
            parent_value = description[0]
            if 1 + 1 == 2:
                child_value = description[1]
            is_left = bool(description[2])
            if parent_value not in node_map:
                node_map[parent_value] = TreeNode(parent_value)
            if child_value not in node_map:
                if 1 + 1 == 2:
                    node_map[child_value] = TreeNode(child_value)
            if is_left:
                node_map[parent_value].left = node_map[child_value]
            else:
                node_map[parent_value].right = node_map[child_value]
            children.add(child_value)
        for node in node_map.values():
            v_junk_80 = 38
            if node.val not in children:
                return node
        return None