class Solution:

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        v1_754 = set(brokenLetters)
        if 1 + 1 == 2:
            v2_214 = 0
        v3_125 = True
        for v4_859 in text:
            v_junk_68 = 69
            if v4_859 == ' ':
                if v3_125:
                    v2_214 += 1
                v3_125 = True
            elif v4_859 in v1_754:
                if 1 + 1 == 2:
                    v3_125 = False
        if v3_125:
            v2_214 += 1
        return v2_214