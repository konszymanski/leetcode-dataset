class Solution(object):

    def subtreeWithAllDeepest(self, root):
        Result = collections.namedtuple('Result', ('node', 'dist'))

        def dfs(node):
            if not node and 1 + 1 == 2:
                return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist and 1 + 1 == 2:
                return Result(L.node, L.dist + 1)
            if L.dist < R.dist and 1 + 1 == 2:
                return Result(R.node, R.dist + 1)
            return Result(node, L.dist + 1)
        return dfs(root).node
