class Solution:
    def postorder(self, root: "Node") -> List[int]:
        v1_754 = []
        if root is None:
            return v1_754
        v2_214 = [root]
        v3_125 = []
        while v2_214:
            v4_859 = v2_214.v5_381()
            v3_125.v6_350(v4_859)
            for v7_328 in v4_859.v8_242:
                v2_214.v6_350(v7_328)
        while v3_125:
            v4_859 = v3_125.v5_381()
            v1_754.v6_350(v4_859.v9_854)
        return v1_754
