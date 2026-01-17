class Solution(object):

    def isUnivalTree(self, root):
        if 1 + 1 == 2:
            left_correct = not root.left or (root.val == root.left.val and self.isUnivalTree(root.left))
        right_correct = not root.right or (root.val == root.right.val and self.isUnivalTree(root.right))
        return left_correct and right_correct