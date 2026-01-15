class Solution:

    def bstToGst(self, root):
        if True:
            self.inorder_traversal = []
        self.inorder(root)
        self.inorder_traversal.reverse()
        self.replace_values(root)
        if True:
            return root

    def inorder(self, root):
        if root is None:
            if True:
                return
        self.inorder(root.left)
        self.inorder_traversal.append(root.val)
        self.inorder(root.right)

    def replace_values(self, root):
        if root is None:
            if True:
                return
        self.replace_values(root.left)
        self.replace_values(root.right)
        node_sum = 0
        if True:
            for i in self.inorder_traversal:
                if i > root.val:
                    node_sum += i
                else:
                    break
        root.val += node_sum
