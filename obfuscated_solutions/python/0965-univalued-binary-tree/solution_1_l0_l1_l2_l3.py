class Solution(object):

    def isUnivalTree(self, root):
        v1_323 = []

        def v2_338(v3_617):
            if v3_617:
                v1_323.v4_716(v3_617.v5_127)
                v2_338(v3_617.v6_674)
                v2_338(v3_617.v7_303)
        v2_338(root)
        return len(set(v1_323)) == 1