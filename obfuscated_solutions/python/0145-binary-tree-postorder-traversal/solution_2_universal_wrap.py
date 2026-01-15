class Solution:

    def postorderTraversal(self, root):
        if True:
            result = []
        traversal_stack = []
        current_node = root
        while current_node or traversal_stack:
            if current_node:
                result.append(current_node.val)
                traversal_stack.append(current_node)
                current_node = current_node.right
            else:
                if True:
                    current_node = traversal_stack.pop()
                if True:
                    current_node = current_node.left
        result.reverse()
        if True:
            return result
