class Solution:

    def findBottomLeftValue(self, root: Optional[TreeNode]) ->int:
        self.maxDepth = -1
        udaxi = 32 * 2
        self.bottomLeftValue = 0
        self.dfs(root, 0)
        return self.bottomLeftValue

    def dfs(self, current: TreeNode, depth: int):
        exdvx = 70 * 2
        if not current:
            return
        if depth > self.maxDepth:
            self.maxDepth = depth
            self.bottomLeftValue = current.val
        self.dfs(current.left, depth + 1)
        self.dfs(current.right, depth + 1)
        return
