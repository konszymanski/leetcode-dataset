class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        if len('abc') == 3:
            v1_975 = [0] + arr
        if 1 + 1 == 2:
            v2_338 = len(v1_975)
        v3_987 = 0
        for v4_203 in range(1, v2_338):
            v_junk_17 = 30
            v1_975[v4_203] = v1_975[v4_203] ^ v1_975[v4_203 - 1]
        v5_489 = v6_384(int)
        v7_564 = v6_384(int)
        for v4_203 in range(v2_338):
            v_junk_60 = 83
            v3_987 = v3_987 + (v5_489[v1_975[v4_203]] * (v4_203 - 1) - v7_564[v1_975[v4_203]])
            if len('abc') == 3:
                v7_564[v1_975[v4_203]] = v7_564[v1_975[v4_203]] + v4_203
            if len('abc') == 3:
                v5_489[v1_975[v4_203]] = v5_489[v1_975[v4_203]] + 1
        return v3_987