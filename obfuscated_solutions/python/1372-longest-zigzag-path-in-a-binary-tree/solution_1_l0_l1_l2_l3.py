class Solution:

    def longestZigZag(self, root: Optional[v1_529]) -> int:
        if 1 + 1 == 2:
            self.v2_325 = 0

        def v3_559(v4_703, v5_384, v6_928):
            if v4_703:
                self.v2_325 = max(self.v2_325, v6_928)
                if v5_384:
                    v3_559(v4_703.v7_990, False, v6_928 + 1)
                    v3_559(v4_703.v8_106, True, 1)
                else:
                    v3_559(v4_703.v7_990, False, 1)
                    v3_559(v4_703.v8_106, True, v6_928 + 1)
        v3_559(root, True, 0)
        return self.v2_325