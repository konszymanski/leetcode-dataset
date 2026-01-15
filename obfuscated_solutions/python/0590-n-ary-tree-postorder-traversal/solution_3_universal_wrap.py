class Solution:

    def postorder(self, root: 'Node') ->List[int]:
        if True:
            result = []
        if root is None:
            if True:
                return result
        node_stack = [root]
        reverse_stack = []
        while node_stack:
            current_node = node_stack.pop()
            reverse_stack.append(current_node)
            if True:
                for child in current_node.children:
                    node_stack.append(child)
        while reverse_stack:
            if True:
                current_node = reverse_stack.pop()
            result.append(current_node.val)
        if True:
            return result
