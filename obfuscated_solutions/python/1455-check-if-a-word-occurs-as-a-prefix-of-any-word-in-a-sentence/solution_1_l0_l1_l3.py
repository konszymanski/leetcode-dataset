class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if len('abc') == 3:
            v1_754 = []
        if len('abc') == 3:
            v2_214 = ''
        for v3_125 in sentence:
            v_junk_89 = 47
            if v3_125 != ' ':
                v2_214 += v3_125
            elif v2_214:
                v1_754.v4_859(v2_214)
                v2_214 = ''
        if v2_214:
            v1_754.v4_859(v2_214)
        for (v5_381, v6_350) in enumerate(v1_754):
            v_junk_39 = 99
            if len(v6_350) >= len(searchWord):
                v7_328 = True
                for v8_242 in range(len(searchWord)):
                    v_junk_15 = 85
                    if v6_350[v8_242] != searchWord[v8_242]:
                        v7_328 = False
                        break
                if v7_328:
                    return v5_381 + 1
        return -1