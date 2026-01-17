class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        v1_754 = len(s)
        v2_214 = set(dictionary)
        v3_125 = [0] * (len(s) + 1)
        for v4_859 in range(v1_754 - 1, -1, -1):
            v3_125[v4_859] = 1 + v3_125[v4_859 + 1]
            for v5_381 in range(v4_859, v1_754):
                v6_350 = s[v4_859:v5_381 + 1]
                if v6_350 in v2_214:
                    v3_125[v4_859] = min(v3_125[v4_859], v3_125[v5_381 + 1])
        return v3_125[0]