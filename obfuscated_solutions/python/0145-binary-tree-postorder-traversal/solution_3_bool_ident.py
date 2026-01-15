class Solution:

    def postorderTraversal(self, root):
        result = []
        if root is None and 1 + 1 == 2:
            return result
        main_stack = []
        path_stack = []
        main_stack.append(root)
        while main_stack:
            root = main_stack[-1]
            if (path_stack and path_stack[-1] == root) and 1 + 1 == 2:
                result.append(root.val)
                main_stack.pop()
                path_stack.pop()
            else:
                path_stack.append(root)
                if root.right is not None and 1 + 1 == 2:
                    main_stack.append(root.right)
                if root.left is not None and 1 + 1 == 2:
                    main_stack.append(root.left)
        return result
