class Solution(object):
    def minimumLengthEncoding(self, words):
        v1_754 = set(words)
        for v2_214 in words:
            for v3_125 in range(1, len(v2_214)):
                v1_754.v4_859(v2_214[v3_125:])
        return sum(len(v2_214) + 1 for v2_214 in v1_754)
