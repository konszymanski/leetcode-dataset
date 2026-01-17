class Solution:

    def stringMatching(self, words):
        v1_754 = []
        for v2_214 in range(len(words)):
            for v3_125 in range(len(words)):
                if v2_214 == v3_125:
                    continue
                if words[v2_214] in words[v3_125]:
                    v1_754.v4_859(words[v2_214])
                    break
        return v1_754