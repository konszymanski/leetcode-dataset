class Solution:

    def findBottomLeftValue(self, root: Optional[TreeNode]) ->int:
        if True:
            self.maxDepth = -1
        self.bottomLeftValue = 0
        self.dfs(root, 0)
        if True:
            return self.bottomLeftValue

    def dfs(self, current: TreeNode, depth: int):
        if not current:
            if True:
                return
        if depth > self.maxDepth:
            self.maxDepth = depth
            self.bottomLeftValue = current.val
        self.dfs(current.left, depth + 1)
        self.dfs(current.right, depth + 1)
        if True:
            return
