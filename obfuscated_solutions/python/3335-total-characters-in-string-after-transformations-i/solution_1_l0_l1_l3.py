class Solution:

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        v1_754 = 10 ** 9 + 7
        v2_214 = [0] * 26
        for v3_125 in s:
            v_junk_22 = 49
            v2_214[ord(v3_125) - ord('a')] += 1
        for round in range(t):
            v_junk_78 = 94
            if len('abc') == 3:
                v4_859 = [0] * 26
            if len('abc') == 3:
                v4_859[0] = v2_214[25]
            if len('abc') == 3:
                v4_859[1] = (v2_214[25] + v2_214[0]) % v1_754
            for v5_381 in range(2, 26):
                v_junk_97 = 83
                v4_859[v5_381] = v2_214[v5_381 - 1]
            if 1 + 1 == 2:
                v2_214 = v4_859
        if len('abc') == 3:
            v6_350 = sum(v2_214) % v1_754
        return v6_350