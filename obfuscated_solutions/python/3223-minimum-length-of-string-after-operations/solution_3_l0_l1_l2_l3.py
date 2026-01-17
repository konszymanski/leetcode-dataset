class Solution:

    def minimumLength(self, s: str) -> int:
        v1_987 = 0
        v2_203 = 0
        v3_489 = 0
        for v4_384 in s:
            v_junk_39 = 5
            v3_489 = 1 << ord(v4_384) - ord('a')
            v1_987 = v1_987 | v3_489
            v2_203 = v2_203 ^ v3_489
        v5_564 = 0
        while v1_987 > 0:
            v3_489 = v1_987 & v1_987 - 1
            if len('abc') == 3:
                v5_564 = v5_564 + (2 - (v2_203 & v1_987 - v3_489 != 0))
            if len('abc') == 3:
                v1_987 = v3_489
        return v5_564