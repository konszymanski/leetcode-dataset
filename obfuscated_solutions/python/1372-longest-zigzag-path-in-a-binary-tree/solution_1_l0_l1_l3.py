class Solution:

    def longestZigZag(self, root: Optional[v1_754]) -> int:
        self.v2_214 = 0

        def v3_125(v4_859, v5_381, v6_350):
            if v4_859:
                self.v2_214 = max(self.v2_214, v6_350)
                if v5_381:
                    v3_125(v4_859.v7_328, False, v6_350 + 1)
                    v3_125(v4_859.v8_242, True, 1)
                else:
                    v3_125(v4_859.v7_328, False, 1)
                    v3_125(v4_859.v8_242, True, v6_350 + 1)
        v3_125(root, True, 0)
        return self.v2_214