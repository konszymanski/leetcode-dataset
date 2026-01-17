class Solution(object):

    def isUnivalTree(self, root):
        if 1 + 1 == 2:
            v1_818 = not root.v2_658 or (root.v3_529 == root.v2_658.v3_529 and self.isUnivalTree(root.v2_658))
        v4_325 = not root.v5_559 or (root.v3_529 == root.v5_559.v3_529 and self.isUnivalTree(root.v5_559))
        return v1_818 and v4_325