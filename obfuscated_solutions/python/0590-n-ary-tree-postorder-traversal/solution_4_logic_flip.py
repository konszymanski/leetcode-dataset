class Solution:

    def postorder(self, root: 'Node') ->List[int]:
        result = []
        if root is None:
            return result
        node_stack = [(root, False)]
        while node_stack:
            current_node, is_visited = node_stack.pop()
            if is_visited:
                result.append(current_node.val)
            else:
                node_stack.append((current_node, True))
                for child in reversed(current_node.children):
                    node_stack.append((child, False))
        return result
