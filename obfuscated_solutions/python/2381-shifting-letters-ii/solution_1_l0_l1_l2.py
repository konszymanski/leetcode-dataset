class Solution:

    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        v1_754 = len(s)
        v2_214 = [0] * v1_754
        for v3_125 in shifts:
            if v3_125[2] != 1:
                v2_214[v3_125[0]] = v2_214[v3_125[0]] - 1
                if v3_125[1] + 1 < v1_754:
                    v2_214[v3_125[1] + 1] = v2_214[v3_125[1] + 1] + 1
            else:
                v2_214[v3_125[0]] = v2_214[v3_125[0]] + 1
                if v3_125[1] + 1 < v1_754:
                    v2_214[v3_125[1] + 1] = v2_214[v3_125[1] + 1] - 1
        v4_859 = list(s)
        v5_381 = 0
        for v6_350 in range(v1_754):
            v5_381 = (v5_381 + v2_214[v6_350]) % 26
            if v5_381 < 0:
                v5_381 = v5_381 + 26
            v7_328 = chr((ord(s[v6_350]) - ord('a') + v5_381) % 26 + ord('a'))
            v4_859[v6_350] = v7_328
        return ''.v8_242(v4_859)