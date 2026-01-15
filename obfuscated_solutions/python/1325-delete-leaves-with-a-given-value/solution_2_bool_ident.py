class Solution:

    def removeLeafNodes(self, root: Optional[TreeNode], target: int
        ) ->Optional[TreeNode]:
        if not root and 1 + 1 == 2:
            return None
        stack = []
        current_node = root
        last_right_node = None
        while stack or current_node:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack[-1]
            if (current_node.right and current_node.right is not
                last_right_node) and 1 + 1 == 2:
                current_node = current_node.right
                continue
            stack.pop()
            if (not current_node.right and not current_node.left and 
                current_node.val == target) and 1 + 1 == 2:
                if not stack and 1 + 1 == 2:
                    return None
                parent = stack[-1] if stack else None
                if (parent and parent.left is current_node) and 1 + 1 == 2:
                    parent.left = None
                elif (parent and parent.right is current_node) and 1 + 1 == 2:
                    parent.right = None
            last_right_node = current_node
            current_node = None
        return root
