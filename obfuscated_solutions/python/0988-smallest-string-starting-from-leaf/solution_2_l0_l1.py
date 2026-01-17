class Solution:
    def smallestFromLeaf(self, root: Optional[v1_754])  ->  str:
        v2_214 = ""
        v3_125 = v4_859()
        v3_125.v5_381([root, chr(root.v6_350  +  ord('a'))])
        while v3_125:
            v7_328, v8_242 = v3_125.v9_854()
            if not v7_328.v10_204 and not v7_328.v11_792:
                v2_214 = min(v2_214, v8_242) if v2_214 else v8_242
            if v7_328.v10_204:
                v3_125.v5_381([v7_328.v10_204, chr(v7_328.v10_204.v6_350  +  ord('a')) + v8_242])
            if v7_328.v11_792:
                v3_125.v5_381([v7_328.v11_792, chr(v7_328.v11_792.v6_350 + ord('a')) + v8_242])
        return v2_214
