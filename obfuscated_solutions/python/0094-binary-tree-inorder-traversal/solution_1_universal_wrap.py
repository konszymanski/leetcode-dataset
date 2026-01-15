class Solution:

    def inorderTraversal(self, root):
        if True:
            res = []
        self.helper(root, res)
        if True:
            return res

    def helper(self, root, res):
        if root is not None:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
