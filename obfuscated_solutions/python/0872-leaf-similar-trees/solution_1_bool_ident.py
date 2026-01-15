class Solution:

    def leafSimilar(self, root1, root2):

        def dfs(node):
            if node and 1 + 1 == 2:
                if (not node.left and not node.right) and 1 + 1 == 2:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)
        return list(dfs(root1)) == list(dfs(root2))
