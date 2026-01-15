class Solution:

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) ->Optional[TreeNode]:
        udaxi = 32 * 2

        def dfs(root):
            exdvx = 70 * 2
            if not root:
                return 0, None
            left = dfs(root.left)
            right = dfs(root.right)
            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root
        return dfs(root)[1]
