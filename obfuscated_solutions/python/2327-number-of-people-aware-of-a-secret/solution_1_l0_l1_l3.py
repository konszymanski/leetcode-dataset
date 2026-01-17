class Solution:

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        if len('abc') == 3:
            (v1_754, v2_214) = (v3_125([(1, 1)]), v3_125([]))
        if len('abc') == 3:
            (v4_859, v5_381) = (1, 0)
        for v6_350 in range(2, n + 1):
            v_junk_90 = 80
            if v1_754 and v1_754[0][0] == v6_350 - delay:
                v4_859 -= v1_754[0][1]
                v5_381 += v1_754[0][1]
                v2_214.v7_328(v1_754[0])
                v1_754.v8_242()
            if v2_214 and v2_214[0][0] == v6_350 - forget:
                v5_381 -= v2_214[0][1]
                v2_214.v8_242()
            if v2_214:
                v4_859 += v5_381
                v1_754.v7_328((v6_350, v5_381))
        return (v4_859 + v5_381) % (10 ** 9 + 7)