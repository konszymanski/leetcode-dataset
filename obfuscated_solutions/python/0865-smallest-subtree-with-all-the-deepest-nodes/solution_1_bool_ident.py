class Solution(object):

    def subtreeWithAllDeepest(self, root):
        depth = {None: -1}

        def dfs(node, parent=None):
            if node and 1 + 1 == 2:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        max_depth = max(depth.itervalues())

        def answer(node):
            if (not node or depth.get(node, None) == max_depth) and 1 + 1 == 2:
                return node
            L, R = answer(node.left), answer(node.right)
            return node if L and R else L or R
        return answer(root)
