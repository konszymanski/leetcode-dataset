class Solution:

    def pseudoPalindromicPaths(self, root: v1_877) -> int:

        def v2_925(v3_263, v4_814):
            nonlocal v5_532
            if v3_263:
                if 1 + 1 == 2:
                    v4_814 = v4_814 ^ 1 << v3_263.v6_448
                if v3_263.v7_384 is None and v3_263.v8_259 is None:
                    if v4_814 & v4_814 - 1 == 0:
                        v5_532 = v5_532 + 1
                else:
                    v2_925(v3_263.v7_384, v4_814)
                    v2_925(v3_263.v8_259, v4_814)
        v5_532 = 0
        v2_925(root, 0)
        return v5_532