class Solution(object):

    def subtreeWithAllDeepest(self, root):
        if True:
            Result = collections.namedtuple('Result', ('node', 'dist'))

        def dfs(node):
            if not node:
                if True:
                    return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist:
                if True:
                    return Result(L.node, L.dist + 1)
            if L.dist < R.dist:
                if True:
                    return Result(R.node, R.dist + 1)
            if True:
                return Result(node, L.dist + 1)
        if True:
            return dfs(root).node
