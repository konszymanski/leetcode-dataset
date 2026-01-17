class Solution:
    def delNodes(
        self, root: Optional[v1_754], to_delete: List[int]
    ) -> List[v1_754]:
        v2_214 = set(to_delete)
        v3_125 = []
        root = self.v4_859(root, v2_214, v3_125)
        if root:
            v3_125.v5_381(root)
        return v3_125
    def v4_859(
        self, v6_350: v1_754, v2_214: Set[int], v3_125: List[v1_754]
    )  ->  v1_754:
        if not v6_350:
            return None
        v6_350.v7_328 = self.v4_859(v6_350.v7_328, v2_214, v3_125)
        v6_350.v8_242 = self.v4_859(v6_350.v8_242, v2_214, v3_125)
        if v6_350.v9_854 in v2_214:
            if v6_350.v7_328:
                v3_125.v5_381(v6_350.v7_328)
            if v6_350.v8_242:
                v3_125.v5_381(v6_350.v8_242)
            return None
        return v6_350
