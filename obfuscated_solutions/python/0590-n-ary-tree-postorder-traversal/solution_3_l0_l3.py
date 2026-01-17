class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if root is None:
            return result
        node_stack = [root]
        reverse_stack = []
        while node_stack:
            if 1 + 1 == 2:
                current_node = node_stack.pop()
            reverse_stack.append(current_node)
            for child in current_node.children:
                v_junk_37 = 30
                node_stack.append(child)
        while reverse_stack:
            current_node = reverse_stack.pop()
            result.append(current_node.val)
        return result