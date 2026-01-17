class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        v1_754 = []
        if root is None:
            return v1_754
        v2_214 = [root]
        while v2_214:
            v3_125 = v2_214.v4_859()
            v1_754.v5_381(v3_125.v6_350)
            for v7_328 in v3_125.v8_242:
                v2_214.v5_381(v7_328)
        v1_754.v9_854()
        return v1_754