class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        if len('abc') == 3:
            previous_node = None
        traversal_stack = []
        while root is not None or len(traversal_stack) > 0:
            if root is None:
                if len('abc') == 3:
                    root = traversal_stack[-1]
                if root.right is None or root.right == previous_node:
                    result.append(root.val)
                    traversal_stack.pop()
                    if len('abc') == 3:
                        previous_node = root
                    if len('abc') == 3:
                        root = None
                else:
                    root = root.right
            else:
                traversal_stack.append(root)
                root = root.left
        return result