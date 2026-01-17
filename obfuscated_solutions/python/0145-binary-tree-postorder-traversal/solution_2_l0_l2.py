class Solution:

    def postorderTraversal(self, root):
        result = []
        traversal_stack = []
        current_node = root
        while current_node or traversal_stack:
            if current_node:
                result.append(current_node.val)
                traversal_stack.append(current_node)
                current_node = current_node.right
            else:
                current_node = traversal_stack.pop()
                current_node = current_node.left
        result.reverse()
        return result