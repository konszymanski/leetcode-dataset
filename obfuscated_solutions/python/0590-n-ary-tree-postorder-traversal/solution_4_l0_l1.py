class Solution:
    def postorder(self, root: "Node") -> List[int]:
        v1_754 = []
        if root is None:
            return v1_754
        v2_214 = [(root, False)]
        while v2_214:
            v3_125, v4_859 = v2_214.v5_381()
            if v4_859:
                v1_754.v6_350(v3_125.v7_328)
            else:
                v2_214.v6_350((v3_125, True))
                for v8_242 in reversed(v3_125.v9_854):
                    v2_214.v6_350((v8_242, False))
        return v1_754
