class Solution:
    def lcaDeepestLeaves(self, root: Optional[v1_754]) -> Optional[v1_754]:
        def v2_214(root):
            if not root:
                return 0, None
            v3_125 = v2_214(root.v3_125)
            v4_859 = v2_214(root.v4_859)
            if v3_125[0] > v4_859[0]:
                return v3_125[0]  +  1, v3_125[1]
            if v3_125[0]  <  v4_859[0]:
                return v4_859[0]  +  1, v4_859[1]
            return v3_125[0] + 1, root
        return v2_214(root)[1]
