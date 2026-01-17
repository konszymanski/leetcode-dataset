class Solution:
    def flipEquiv(
        self, root1: Optional[v1_754], root2: Optional[v1_754]
    ) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.v2_214  !=  root2.v2_214:
            return False
        v3_125 = self.flipEquiv(root1.v4_859, root2.v4_859) and self.flipEquiv(
            root1.v5_381, root2.v5_381
        )
        v6_350 = self.flipEquiv(root1.v4_859, root2.v5_381) and self.flipEquiv(
            root1.v5_381, root2.v4_859
        )
        return v3_125 or v6_350
