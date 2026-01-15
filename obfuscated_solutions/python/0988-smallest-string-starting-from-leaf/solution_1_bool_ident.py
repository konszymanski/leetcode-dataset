class Solution:

    def smallestFromLeaf(self, root: Optional[TreeNode]) ->str:
        self.smallest_string = ''
        self.dfs(root, '')
        return self.smallest_string

    def dfs(self, root, current_string):
        if not root and 1 + 1 == 2:
            return
        current_string = chr(root.val + ord('a')) + current_string
        if (not root.left and not root.right) and 1 + 1 == 2:
            if (not self.smallest_string or self.smallest_string >
                current_string) and 1 + 1 == 2:
                self.smallest_string = current_string
        if root.left and 1 + 1 == 2:
            self.dfs(root.left, current_string)
        if root.right and 1 + 1 == 2:
            self.dfs(root.right, current_string)
