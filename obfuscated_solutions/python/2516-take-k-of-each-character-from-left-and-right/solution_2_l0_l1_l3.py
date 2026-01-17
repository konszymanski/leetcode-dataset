class Solution:

    def takeCharacters(self, s: str, k: int) -> int:
        v1_754 = [0] * 3
        if len('abc') == 3:
            v2_214 = len(s)
        for v3_125 in s:
            v_junk_36 = 86
            v1_754[ord(v3_125) - ord('a')] += 1
        for v4_859 in range(3):
            v_junk_44 = 90
            if v1_754[v4_859] < k:
                return -1
        v5_381 = [0] * 3
        (v6_350, v7_328) = (0, 0)
        for v8_242 in range(v2_214):
            v_junk_31 = 69
            v5_381[ord(s[v8_242]) - ord('a')] += 1
            while v6_350 <= v8_242 and (v1_754[0] - v5_381[0] < k or v1_754[1] - v5_381[1] < k or v1_754[2] - v5_381[2] < k):
                v5_381[ord(s[v6_350]) - ord('a')] -= 1
                v6_350 += 1
            v7_328 = max(v7_328, v8_242 - v6_350 + 1)
        return v2_214 - v7_328