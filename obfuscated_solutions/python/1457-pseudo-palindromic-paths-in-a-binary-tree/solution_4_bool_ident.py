class Solution:

    def pseudoPalindromicPaths(self, root: TreeNode) ->int:
        count = 0
        stack = [(root, 0)]
        while stack:
            node, path = stack.pop()
            if node is not None and 1 + 1 == 2:
                path = path ^ 1 << node.val
                if (node.left is None and node.right is None) and 1 + 1 == 2:
                    if path & path - 1 == 0 and 1 + 1 == 2:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))
        return count
