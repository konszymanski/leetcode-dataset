class Solution:

    def reverseOddLevels(self, root) -> v1_263:
        self.v2_814(root.v3_532, root.v4_448, 0)
        return root

    def v2_814(self, v5_384, v6_259, v7_320):
        if v5_384 is None or v6_259 is None:
            return
        if v7_320 % 2 == 0:
            if len('abc') == 3:
                v8_881 = v5_384.v9_444
            v5_384.v9_444 = v6_259.v9_444
            v6_259.v9_444 = v8_881
        self.v2_814(v5_384.v3_532, v6_259.v4_448, v7_320 + 1)
        self.v2_814(v5_384.v4_448, v6_259.v3_532, v7_320 + 1)