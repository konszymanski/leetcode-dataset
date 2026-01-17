class Solution:
    def find_canonical_form(self, root: v1_754)  ->  None:
        if not root:
            return
        self.find_canonical_form(root.v2_214)
        self.find_canonical_form(root.v3_125)
        if not root.v3_125:
            return
        if not root.v2_214:
            root.v2_214 = root.v3_125
            root.v3_125 = None
            return
        v2_214 = root.v2_214
        v3_125 = root.v3_125
        if v2_214.v4_859 > v3_125.v4_859:
            root.v2_214, root.v3_125 = root.v3_125, root.v2_214
    def v5_381(self, v6_350: v1_754, v7_328: v1_754)  ->  bool:
        if not v6_350 and not v7_328:
            return True
        if not v6_350 or not v7_328:
            return False
        if v6_350.v4_859  !=  v7_328.v4_859:
            return False
        return self.v5_381(
            v6_350.v2_214, v7_328.v2_214
        ) and self.v5_381(v6_350.v3_125, v7_328.v3_125)
    def v8_242(self, v6_350: v1_754, v7_328: v1_754) -> bool:
        self.find_canonical_form(v6_350)
        self.find_canonical_form(v7_328)
        return self.v5_381(v6_350, v7_328)
