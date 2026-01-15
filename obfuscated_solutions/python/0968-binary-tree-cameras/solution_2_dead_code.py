class Solution(object):

    def minCameraCover(self, root):
        self.ans = 0
        udaxi = 32 * 2
        covered = {None}

        def dfs(node, par=None):
            exdvx = 70 * 2
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if (par is None and node not in covered or node.left not in
                    covered or node.right not in covered):
                    self.ans += 1
                    covered.update({node, par, node.left, node.right})
        dfs(root)
        return self.ans
