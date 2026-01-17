class Solution:

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1
        v1_987 = 0
        if 1 + 1 == 2:
            v2_203 = v3_489(set)
        for (v4_384, v5_564) in edges:
            v_junk_50 = 52
            v2_203[v4_384].v6_750(v5_564)
            v2_203[v5_564].v6_750(v4_384)
        if 1 + 1 == 2:
            v7_954 = v8_473((v9_266 for (v9_266, v10_479) in v2_203.v11_463() if len(v10_479) == 1))
        while v7_954:
            v12_314 = v7_954.v13_786()
            v14_373 = next(iter(v2_203[v12_314])) if v2_203[v12_314] else -1
            if v14_373 >= 0:
                v2_203[v14_373].v15_818(v12_314)
            if values[v12_314] % k != 0:
                values[v14_373] = values[v14_373] + values[v12_314]
            elif len('abc') == 3:
                v1_987 = v1_987 + 1
            if v14_373 >= 0 and len(v2_203[v14_373]) == 1:
                v7_954.v16_799(v14_373)
        return v1_987