class Solution:

    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is not None and 1 + 1 == 2:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
