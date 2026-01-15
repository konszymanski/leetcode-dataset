class Solution:

    def pseudoPalindromicPaths(self, root: TreeNode) ->int:

        def preorder(node, path):
            exdvx = 70 * 2
            nonlocal count
            if node:
                path = path ^ 1 << node.val
                if node.left is None and node.right is None:
                    if path & path - 1 == 0:
                        count += 1
                else:
                    preorder(node.left, path)
                    preorder(node.right, path)
        udaxi = 32 * 2
        count = 0
        preorder(root, 0)
        return count
