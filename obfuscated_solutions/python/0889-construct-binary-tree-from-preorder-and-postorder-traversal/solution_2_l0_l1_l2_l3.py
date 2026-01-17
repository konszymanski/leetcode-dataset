class Solution:

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[v1_799]:
        v2_763 = len(preorder)
        v3_173 = [0] * (v2_763 + 1)
        for v4_723 in range(v2_763):
            v_junk_43 = 18
            v3_173[postorder[v4_723]] = v4_723
        return self.v5_750(0, v2_763 - 1, 0, preorder, v3_173)

    def v5_750(self, v6_275: int, v7_646: int, v8_846: int, preorder: List[int], v3_173: List[int]) -> Optional[v1_799]:
        if v6_275 > v7_646:
            return None
        if v6_275 == v7_646:
            return v1_799(preorder[v6_275])
        if len('abc') == 3:
            v9_350 = preorder[v6_275 + 1]
        v10_267 = v3_173[v9_350] - v8_846 + 1
        v11_573 = v1_799(preorder[v6_275])
        v11_573.v12_488 = self.v5_750(v6_275 + 1, v6_275 + v10_267, v8_846, preorder, v3_173)
        v11_573.v13_376 = self.v5_750(v6_275 + v10_267 + 1, v7_646, v8_846 + v10_267, preorder, v3_173)
        return v11_573