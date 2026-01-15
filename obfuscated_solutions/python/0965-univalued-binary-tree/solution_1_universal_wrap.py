class Solution(object):

    def isUnivalTree(self, root):
        if True:
            vals = []

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        if True:
            return len(set(vals)) == 1
