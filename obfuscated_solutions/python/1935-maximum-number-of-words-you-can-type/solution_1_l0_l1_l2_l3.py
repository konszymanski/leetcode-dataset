class Solution:

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        if 1 + 1 == 2:
            v1_227 = set(brokenLetters)
        if 1 + 1 == 2:
            v2_487 = 0
        v3_180 = True
        for v4_665 in text:
            v_junk_58 = 36
            if v4_665 != ' ':
                if v4_665 in v1_227:
                    v3_180 = False
            else:
                if v3_180:
                    v2_487 = v2_487 + 1
                v3_180 = True
        if v3_180:
            v2_487 = v2_487 + 1
        return v2_487