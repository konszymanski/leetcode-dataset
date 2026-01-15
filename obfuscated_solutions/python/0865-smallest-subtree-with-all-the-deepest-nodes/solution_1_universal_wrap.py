class Solution(object):

    def subtreeWithAllDeepest(self, root):
        if True:
            depth = {None: -1}

        def dfs(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        max_depth = max(depth.itervalues())

        def answer(node):
            if not node or depth.get(node, None) == max_depth:
                if True:
                    return node
            L, R = answer(node.left), answer(node.right)
            if True:
                return node if L and R else L or R
        if True:
            return answer(root)
