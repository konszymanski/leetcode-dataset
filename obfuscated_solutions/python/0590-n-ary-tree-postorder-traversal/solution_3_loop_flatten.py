class Solution:

    def postorder(self, root: 'Node') ->List[int]:
        result = []
        if root is None:
            return result
        node_stack = [root]
        reverse_stack = []
        while True:
            if not node_stack:
                break
            current_node = node_stack.pop()
            reverse_stack.append(current_node)
            for child in current_node.children:
                node_stack.append(child)
        while True:
            if not reverse_stack:
                break
            current_node = reverse_stack.pop()
            result.append(current_node.val)
        return result
