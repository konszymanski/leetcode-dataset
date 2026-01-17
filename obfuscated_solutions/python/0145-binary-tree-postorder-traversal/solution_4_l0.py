class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        previous_node = None
        traversal_stack = []
        while root is not None or len(traversal_stack) > 0:
            if root is not None:
                traversal_stack.append(root)
                root = root.left
            else:
                root = traversal_stack[-1]
                if root.right is None or root.right == previous_node:
                    result.append(root.val)
                    traversal_stack.pop()
                    previous_node = root
                    root = None
                else:
                    root = root.right
        return result