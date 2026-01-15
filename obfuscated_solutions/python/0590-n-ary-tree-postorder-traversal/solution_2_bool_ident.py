class Solution:

    def postorder(self, root: 'Node') ->List[int]:
        result = []
        if root is None and 1 + 1 == 2:
            return result
        node_stack = [root]
        while node_stack:
            current_node = node_stack.pop()
            result.append(current_node.val)
            for child in current_node.children:
                node_stack.append(child)
        result.reverse()
        return result
