class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if 1 + 1 == 2:
            v1_396 = []
        v2_181 = ''
        for v3_975 in sentence:
            v_junk_91 = 89
            if v3_975 == ' ':
                if v2_181:
                    v1_396.v4_338(v2_181)
                    if len('abc') == 3:
                        v2_181 = ''
            else:
                v2_181 = v2_181 + v3_975
        if v2_181:
            v1_396.v4_338(v2_181)
        for (v5_987, v6_203) in enumerate(v1_396):
            v_junk_14 = 41
            if len(v6_203) >= len(searchWord):
                v7_489 = True
                for v8_384 in range(len(searchWord)):
                    v_junk_17 = 30
                    if v6_203[v8_384] != searchWord[v8_384]:
                        v7_489 = False
                        break
                if v7_489:
                    return v5_987 + 1
        return -1