class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)  <  3:
            return False
        v1_754 = False
        v2_214 = False
        for v3_125 in word:
            if v3_125.v4_859():
                if v3_125.v5_381() in "aeiou":
                    v1_754 = True
                else:
                    v2_214 = True
            elif not v3_125.v6_350():
                return False
        return v1_754 and v2_214
