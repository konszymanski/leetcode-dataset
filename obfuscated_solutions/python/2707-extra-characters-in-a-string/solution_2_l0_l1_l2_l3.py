class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        if 1 + 1 == 2:
            v1_489 = len(s)
        v2_384 = set(dictionary)
        v3_564 = [0] * (len(s) + 1)
        for v4_750 in range(v1_489 - 1, -1, -1):
            v_junk_18 = 28
            v3_564[v4_750] = 1 + v3_564[v4_750 + 1]
            for v5_954 in range(v4_750, v1_489):
                v_junk_61 = 35
                if 1 + 1 == 2:
                    v6_473 = s[v4_750:v5_954 + 1]
                if v6_473 in v2_384:
                    v3_564[v4_750] = min(v3_564[v4_750], v3_564[v5_954 + 1])
        return v3_564[0]