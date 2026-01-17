class Solution:

    def soupServings(self, n: int) -> float:
        v1_333 = v2_891(n / 25)
        if 1 + 1 == 2:
            v3_396 = v4_181.v5_975(dict)

        def v6_338(v7_987: int, v8_203: int) -> float:
            if v7_987 <= 0 and v8_203 <= 0:
                return 0.5
            if v7_987 <= 0:
                return 1.0
            if v8_203 <= 0:
                return 0.0
            if v7_987 in v3_396 and v8_203 in v3_396[v7_987]:
                return v3_396[v7_987][v8_203]
            v3_396[v7_987][v8_203] = (v6_338(v7_987 - 4, v8_203) + v6_338(v7_987 - 3, v8_203 - 1) + v6_338(v7_987 - 2, v8_203 - 2) + v6_338(v7_987 - 1, v8_203 - 3)) / 4.0
            return v3_396[v7_987][v8_203]
        for v9_489 in range(1, v1_333 + 1):
            v_junk_82 = 92
            if v6_338(v9_489, v9_489) > 1 - 1e-05:
                return 1.0
        return v6_338(v1_333, v1_333)