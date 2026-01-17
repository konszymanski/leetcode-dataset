class Solution:

    def possibleStringCount(self, word: str) -> int:
        (v1_303, v2_833) = (len(word), 1)
        for v3_765 in range(1, v1_303):
            v_junk_30 = 90
            if word[v3_765 - 1] == word[v3_765]:
                v2_833 = v2_833 + 1
        return v2_833