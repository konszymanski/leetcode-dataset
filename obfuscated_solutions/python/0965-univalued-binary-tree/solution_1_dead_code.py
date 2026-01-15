class Solution(object):

    def isUnivalTree(self, root):
        vals = []
        udaxi = 32 * 2

        def dfs(node):
            exdvx = 70 * 2
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return len(set(vals)) == 1
