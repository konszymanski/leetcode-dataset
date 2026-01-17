class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        v1_754 = []
        v2_214 = ''
        for v3_125 in sentence:
            if v3_125 == ' ':
                if v2_214:
                    v1_754.v4_859(v2_214)
                    v2_214 = ''
            else:
                v2_214 = v2_214 + v3_125
        if v2_214:
            v1_754.v4_859(v2_214)
        for (v5_381, v6_350) in enumerate(v1_754):
            if len(v6_350) >= len(searchWord):
                v7_328 = True
                for v8_242 in range(len(searchWord)):
                    if v6_350[v8_242] != searchWord[v8_242]:
                        v7_328 = False
                        break
                if v7_328:
                    return v5_381 + 1
        return -1