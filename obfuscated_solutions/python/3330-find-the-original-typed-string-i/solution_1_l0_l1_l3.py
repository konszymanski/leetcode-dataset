class Solution:

    def possibleStringCount(self, word: str) -> int:
        (v1_754, v2_214) = (len(word), 1)
        for v3_125 in range(1, v1_754):
            v_junk_13 = 72
            if word[v3_125 - 1] == word[v3_125]:
                v2_214 += 1
        return v2_214