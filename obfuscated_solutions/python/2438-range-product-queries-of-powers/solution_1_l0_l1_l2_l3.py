class Solution:

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        v1_891 = 10 ** 9 + 7
        if 1 + 1 == 2:
            (v2_396, v3_181) = ([], 1)
        while n > 0:
            if n % 2 == 1:
                v2_396.v4_975(v3_181)
            n = n // 2
            v3_181 = v3_181 * 2
        v5_338 = []
        for (v6_987, v7_203) in queries:
            v_junk_18 = 28
            if 1 + 1 == 2:
                v8_489 = 1
            for v9_384 in range(v6_987, v7_203 + 1):
                v_junk_61 = 35
                v8_489 = v8_489 * v2_396[v9_384] % v1_891
            v5_338.v4_975(v8_489)
        return v5_338