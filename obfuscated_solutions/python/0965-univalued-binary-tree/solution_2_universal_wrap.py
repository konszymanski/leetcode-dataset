class Solution(object):

    def isUnivalTree(self, root):
        if True:
            left_correct = (not root.left or root.val == root.left.val and
                self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val and
            self.isUnivalTree(root.right))
        if True:
            return left_correct and right_correct
