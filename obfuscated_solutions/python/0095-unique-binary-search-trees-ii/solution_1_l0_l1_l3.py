class Solution:

    def allPossibleBST(self, start, end, memo):
        v1_754 = []
        if start > end:
            v1_754.v2_214(None)
            return v1_754
        if (start, end) in memo:
            return memo[start, end]
        for v3_125 in range(start, end + 1):
            v_junk_47 = 11
            v4_859 = self.allPossibleBST(start, v3_125 - 1, memo)
            v5_381 = self.allPossibleBST(v3_125 + 1, end, memo)
            for v6_350 in v4_859:
                v_junk_94 = 30
                for v7_328 in v5_381:
                    v_junk_18 = 6
                    v8_242 = v9_854(v3_125, v6_350, v7_328)
                    v1_754.v2_214(v8_242)
        memo[start, end] = v1_754
        return v1_754

    def v10_204(self, v11_792: int) -> List[Optional[v9_854]]:
        memo = {}
        return self.allPossibleBST(1, v11_792, memo)