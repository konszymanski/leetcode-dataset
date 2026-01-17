class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    )  ->  Optional[v1_754]:
        v2_214 = len(preorder)
        return self.v3_125(0, v2_214 - 1, 0, preorder, postorder)
    def v3_125(
        self,
        v4_859: int,
        v5_381: int,
        v6_350: int,
        preorder: List[int],
        postorder: List[int],
    )  ->  Optional[v1_754]:
        if v4_859  >  v5_381:
            return None
        if v4_859  ==  v5_381:
            return v1_754(preorder[v4_859])
        v7_328 = preorder[v4_859  +  1]
        v8_242 = 1
        while postorder[v6_350  +  v8_242  -  1] != v7_328:
            v8_242 += 1
        v9_854 = v1_754(preorder[v4_859])
        v9_854.v10_204 = self.v3_125(
            v4_859 + 1,
            v4_859 + v8_242,
            v6_350,
            preorder,
            postorder,
        )
        v9_854.v11_792 = self.v3_125(
            v4_859 + v8_242  +  1,
            v5_381,
            v6_350  +  v8_242,
            preorder,
            postorder,
        )
        return v9_854
