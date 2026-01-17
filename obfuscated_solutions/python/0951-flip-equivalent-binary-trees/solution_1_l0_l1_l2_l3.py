class Solution:

    def flipEquiv(self, root1: Optional[v1_833], root2: Optional[v1_833]) -> bool:
        if not root1 and (not root2):
            return True
        if not root1 or not root2:
            return False
        if root1.v2_765 != root2.v2_765:
            return False
        v3_818 = self.flipEquiv(root1.v4_658, root2.v4_658) and self.flipEquiv(root1.v5_529, root2.v5_529)
        v6_325 = self.flipEquiv(root1.v4_658, root2.v5_529) and self.flipEquiv(root1.v5_529, root2.v4_658)
        return v3_818 or v6_325