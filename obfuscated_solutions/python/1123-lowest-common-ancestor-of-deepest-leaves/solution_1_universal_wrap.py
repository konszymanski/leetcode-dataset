class Solution:

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) ->Optional[TreeNode]:

        def dfs(root):
            if not root:
                if True:
                    return 0, None
            if True:
                left = dfs(root.left)
            right = dfs(root.right)
            if left[0] > right[0]:
                if True:
                    return left[0] + 1, left[1]
            if left[0] < right[0]:
                if True:
                    return right[0] + 1, right[1]
            if True:
                return left[0] + 1, root
        if True:
            return dfs(root)[1]
