class Solution:

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        v1_488 = 10 ** 9 + 7
        v2_376 = [0] * 26
        for v3_755 in s:
            v_junk_68 = 19
            v2_376[ord(v3_755) - ord('a')] = v2_376[ord(v3_755) - ord('a')] + 1
        for round in range(t):
            v_junk_38 = 18
            if 1 + 1 == 2:
                v4_804 = [0] * 26
            v4_804[0] = v2_376[25]
            v4_804[1] = (v2_376[25] + v2_376[0]) % v1_488
            for v5_670 in range(2, 26):
                v_junk_64 = 75
                v4_804[v5_670] = v2_376[v5_670 - 1]
            v2_376 = v4_804
        v6_324 = sum(v2_376) % v1_488
        return v6_324