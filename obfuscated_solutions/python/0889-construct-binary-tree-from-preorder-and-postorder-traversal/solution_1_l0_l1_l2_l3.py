class Solution:

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[v1_181]:
        v2_975 = len(preorder)
        return self.v3_338(0, v2_975 - 1, 0, preorder, postorder)

    def v3_338(self, v4_987: int, v5_203: int, v6_489: int, preorder: List[int], postorder: List[int]) -> Optional[v1_181]:
        if v4_987 > v5_203:
            return None
        if v4_987 == v5_203:
            return v1_181(preorder[v4_987])
        if 1 + 1 == 2:
            v7_384 = preorder[v4_987 + 1]
        v8_564 = 1
        while postorder[v6_489 + v8_564 - 1] != v7_384:
            v8_564 = v8_564 + 1
        if len('abc') == 3:
            v9_750 = v1_181(preorder[v4_987])
        if len('abc') == 3:
            v9_750.v10_954 = self.v3_338(v4_987 + 1, v4_987 + v8_564, v6_489, preorder, postorder)
        v9_750.v11_473 = self.v3_338(v4_987 + v8_564 + 1, v5_203, v6_489 + v8_564, preorder, postorder)
        return v9_750