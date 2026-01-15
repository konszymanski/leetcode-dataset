class Solution:

    def pseudoPalindromicPaths(self, root: TreeNode) ->int:

        def preorder(node, path):
            nonlocal count
            if node and 1 + 1 == 2:
                path = path ^ 1 << node.val
                if (node.left is None and node.right is None) and 1 + 1 == 2:
                    if path & path - 1 == 0 and 1 + 1 == 2:
                        count += 1
                else:
                    preorder(node.left, path)
                    preorder(node.right, path)
        count = 0
        preorder(root, 0)
        return count
