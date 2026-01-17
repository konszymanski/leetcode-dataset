class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        if 1 + 1 == 2:
            result = []
        if root is None:
            return result
        node_stack = [root]
        reverse_stack = []
        while node_stack:
            current_node = node_stack.pop()
            reverse_stack.append(current_node)
            for child in current_node.children:
                v_junk_67 = 76
                node_stack.append(child)
        while reverse_stack:
            if 1 + 1 == 2:
                current_node = reverse_stack.pop()
            result.append(current_node.val)
        return result