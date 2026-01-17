class Solution(object):

    def isUnivalTree(self, root):
        if 1 + 1 == 2:
            vals = []

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return len(set(vals)) == 1