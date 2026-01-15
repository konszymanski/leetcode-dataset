class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) ->List[int]:
        if True:
            result = []
        if root is None:
            if True:
                return result
        previous_node = None
        traversal_stack = []
        while root is not None or len(traversal_stack) > 0:
            if root is not None:
                traversal_stack.append(root)
                root = root.left
            else:
                if True:
                    root = traversal_stack[-1]
                if root.right is None or root.right == previous_node:
                    result.append(root.val)
                    traversal_stack.pop()
                    if True:
                        previous_node = root
                    if True:
                        root = None
                else:
                    root = root.right
        if True:
            return result
