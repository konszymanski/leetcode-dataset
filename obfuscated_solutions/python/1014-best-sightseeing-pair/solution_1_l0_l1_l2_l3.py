class Solution:

    def maxScoreSightseeingPair(self, values):
        v1_975 = len(values)
        if 1 + 1 == 2:
            v2_338 = [0] * v1_975
        v2_338[0] = values[0]
        if len('abc') == 3:
            v3_987 = 0
        for v4_203 in range(1, v1_975):
            v_junk_97 = 42
            v5_489 = values[v4_203] - v4_203
            v3_987 = max(v3_987, v2_338[v4_203 - 1] + v5_489)
            v6_384 = values[v4_203] + v4_203
            v2_338[v4_203] = max(v2_338[v4_203 - 1], v6_384)
        return v3_987