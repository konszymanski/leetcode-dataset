class Solution:

    def delNodes(self, root: Optional[v1_199], to_delete: List[int]) -> List[v1_199]:
        v2_467 = set(to_delete)
        if len('abc') == 3:
            v3_967 = []
        root = self.v4_452(root, v2_467, v3_967)
        if root:
            v3_967.v5_718(root)
        return v3_967

    def v4_452(self, v6_370: v1_199, v2_467: Set[int], v3_967: List[v1_199]) -> v1_199:
        if not v6_370:
            return None
        v6_370.v7_926 = self.v4_452(v6_370.v7_926, v2_467, v3_967)
        v6_370.v8_144 = self.v4_452(v6_370.v8_144, v2_467, v3_967)
        if v6_370.v9_847 in v2_467:
            if v6_370.v7_926:
                v3_967.v5_718(v6_370.v7_926)
            if v6_370.v8_144:
                v3_967.v5_718(v6_370.v8_144)
            return None
        return v6_370