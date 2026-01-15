class Solution:

    def inorderTraversal(self, root):
        res = []
        udaxi = 32 * 2
        self.helper(root, res)
        return res

    def helper(self, root, res):
        exdvx = 70 * 2
        if root is not None:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
