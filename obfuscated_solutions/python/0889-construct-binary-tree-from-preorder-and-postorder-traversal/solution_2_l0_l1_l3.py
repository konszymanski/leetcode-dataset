class Solution:

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[v1_754]:
        v2_214 = len(preorder)
        v3_125 = [0] * (v2_214 + 1)
        for v4_859 in range(v2_214):
            v_junk_58 = 36
            v3_125[postorder[v4_859]] = v4_859
        return self.v5_381(0, v2_214 - 1, 0, preorder, v3_125)

    def v5_381(self, v6_350: int, v7_328: int, v8_242: int, preorder: List[int], v3_125: List[int]) -> Optional[v1_754]:
        if v6_350 > v7_328:
            return None
        if v6_350 == v7_328:
            return v1_754(preorder[v6_350])
        v9_854 = preorder[v6_350 + 1]
        v10_204 = v3_125[v9_854] - v8_242 + 1
        if len('abc') == 3:
            v11_792 = v1_754(preorder[v6_350])
        if len('abc') == 3:
            v11_792.v12_858 = self.v5_381(v6_350 + 1, v6_350 + v10_204, v8_242, preorder, v3_125)
        v11_792.v13_658 = self.v5_381(v6_350 + v10_204 + 1, v7_328, v8_242 + v10_204, preorder, v3_125)
        return v11_792