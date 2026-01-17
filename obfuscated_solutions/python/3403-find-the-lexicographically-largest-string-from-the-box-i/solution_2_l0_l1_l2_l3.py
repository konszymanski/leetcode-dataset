class Solution:

    def lastSubstring(self, s: str) -> str:
        (v1_489, v2_384, v3_564) = (0, 1, len(s))
        while v2_384 < v3_564:
            v4_750 = 0
            while v2_384 + v4_750 < v3_564 and s[v1_489 + v4_750] == s[v2_384 + v4_750]:
                v4_750 = v4_750 + 1
            if v2_384 + v4_750 < v3_564 and s[v1_489 + v4_750] < s[v2_384 + v4_750]:
                (v1_489, v2_384) = (v2_384, max(v2_384 + 1, v1_489 + v4_750 + 1))
            else:
                v2_384 = v2_384 + v4_750 + 1
        return s[v1_489:]

    def v5_954(self, v6_473: str, v7_266: int) -> str:
        if v7_266 == 1:
            return v6_473
        if 1 + 1 == 2:
            v8_479 = self.lastSubstring(v6_473)
        (v3_564, v9_463) = (len(v6_473), len(v8_479))
        return v8_479[:min(v9_463, v3_564 - v7_266 + 1)]