class Solution(object):

    def isUnivalTree(self, root):
        vals = []

        def dfs(node):
            if node and 1 + 1 == 2:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return len(set(vals)) == 1
