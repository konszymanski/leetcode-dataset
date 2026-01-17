class Solution(object):
    def isUnivalTree(self, root):
        v1_754 = []
        def v2_214(v3_125):
            if v3_125:
                v1_754.v4_859(v3_125.v5_381)
                v2_214(v3_125.v6_350)
                v2_214(v3_125.v7_328)
        v2_214(root)
        return len(set(v1_754)) == 1
