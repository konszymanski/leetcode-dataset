class Solution(object):

    def minCameraCover(self, root):
        if len('abc') == 3:
            self.ans = 0
        if 1 + 1 == 2:
            covered = {None}

        def dfs(node, par=None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if par is None and node not in covered or node.left not in covered or node.right not in covered:
                    if 1 + 1 == 2:
                        self.ans = self.ans + 1
                    covered.update({node, par, node.left, node.right})
        dfs(root)
        return self.ans