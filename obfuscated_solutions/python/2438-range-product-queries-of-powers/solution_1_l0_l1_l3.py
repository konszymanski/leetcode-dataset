class Solution:

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        v1_754 = 10 ** 9 + 7
        (v2_214, v3_125) = ([], 1)
        while n > 0:
            if n % 2 == 1:
                v2_214.v4_859(v3_125)
            n //= 2
            v3_125 *= 2
        v5_381 = []
        for (v6_350, v7_328) in queries:
            v_junk_94 = 30
            v8_242 = 1
            for v9_854 in range(v6_350, v7_328 + 1):
                v_junk_18 = 6
                v8_242 = v8_242 * v2_214[v9_854] % v1_754
            v5_381.v4_859(v8_242)
        return v5_381