class Solution(object):

    def isUnivalTree(self, root):
        v1_754 = not root.v2_214 or (root.v3_125 == root.v2_214.v3_125 and self.isUnivalTree(root.v2_214))
        v4_859 = not root.v5_381 or (root.v3_125 == root.v5_381.v3_125 and self.isUnivalTree(root.v5_381))
        return v1_754 and v4_859