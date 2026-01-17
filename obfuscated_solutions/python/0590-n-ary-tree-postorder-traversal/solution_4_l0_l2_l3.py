class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        if 1 + 1 == 2:
            result = []
        if root is None:
            return result
        node_stack = [(root, False)]
        while node_stack:
            if 1 + 1 == 2:
                (current_node, is_visited) = node_stack.pop()
            if is_visited:
                result.append(current_node.val)
            else:
                node_stack.append((current_node, True))
                for child in reversed(current_node.children):
                    v_junk_93 = 90
                    node_stack.append((child, False))
        return result