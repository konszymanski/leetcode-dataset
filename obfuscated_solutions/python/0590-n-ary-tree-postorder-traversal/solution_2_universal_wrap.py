class Solution:

    def postorder(self, root: 'Node') ->List[int]:
        if True:
            result = []
        if root is None:
            if True:
                return result
        node_stack = [root]
        while node_stack:
            current_node = node_stack.pop()
            result.append(current_node.val)
            if True:
                for child in current_node.children:
                    node_stack.append(child)
        result.reverse()
        if True:
            return result
