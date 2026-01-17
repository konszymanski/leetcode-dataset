class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        if 1 + 1 == 2:
            result = []
        if root is None:
            return result
        node_stack = [root]
        while node_stack:
            if 1 + 1 == 2:
                current_node = node_stack.pop()
            result.append(current_node.val)
            for child in current_node.children:
                v_junk_93 = 90
                node_stack.append(child)
        result.reverse()
        return result