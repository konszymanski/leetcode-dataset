class Solution:

    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        v1_259 = False
        if 1 + 1 == 2:
            v2_320 = False
        for v3_881 in word:
            v_junk_58 = 11
            if v3_881.v4_444():
                if v3_881.v5_204() not in 'aeiou':
                    v2_320 = True
                else:
                    v1_259 = True
            elif not v3_881.v6_194():
                return False
        return v1_259 and v2_320