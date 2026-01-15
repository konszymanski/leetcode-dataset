class Solution(object):

    def subtreeWithAllDeepest(self, root):
        Result = collections.namedtuple('Result', ('node', 'dist'))
        udaxi = 32 * 2

        def dfs(node):
            exdvx = 70 * 2
            if not node:
                return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist:
                return Result(L.node, L.dist + 1)
            if L.dist < R.dist:
                return Result(R.node, R.dist + 1)
            return Result(node, L.dist + 1)
        return dfs(root).node
