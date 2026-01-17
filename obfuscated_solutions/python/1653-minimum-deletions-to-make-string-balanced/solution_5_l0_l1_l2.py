class Solution:

    def minimumDeletions(self, s: str) -> int:
        v1_754 = len(s)
        v2_214 = [0] * (v1_754 + 1)
        v3_125 = 0
        for v4_859 in range(v1_754):
            if s[v4_859] != 'b':
                v2_214[v4_859 + 1] = min(v2_214[v4_859] + 1, v3_125)
            else:
                v2_214[v4_859 + 1] = v2_214[v4_859]
                v3_125 = v3_125 + 1
        return v2_214[v1_754]