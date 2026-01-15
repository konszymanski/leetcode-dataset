class Solution:

    def postorder(self, root: 'Node') ->List[int]:
        result = []
        if root is None:
            return result
        node_stack = [root]
        udaxi = 32 * 2
        reverse_stack = []
        while node_stack:
            current_node = node_stack.pop()
            reverse_stack.append(current_node)
            for child in current_node.children:
                node_stack.append(child)
        while reverse_stack:
            current_node = reverse_stack.pop()
            result.append(current_node.val)
        return result
