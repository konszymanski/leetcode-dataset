class Solution:

    def hasSameDigits(self, s: str) -> bool:
        v1_754 = len(s)
        v2_214 = list(s)
        for v3_125 in range(1, v1_754 - 1):
            for v4_859 in range(v1_754 - v3_125):
                v5_381 = ord(v2_214[v4_859]) - ord('0')
                v6_350 = ord(v2_214[v4_859 + 1]) - ord('0')
                v2_214[v4_859] = chr((v5_381 + v6_350) % 10 + ord('0'))
        return v2_214[0] == v2_214[1]