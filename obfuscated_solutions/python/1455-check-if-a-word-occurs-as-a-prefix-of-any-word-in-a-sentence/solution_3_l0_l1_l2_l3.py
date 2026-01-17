class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        v1_127 = sentence.v2_674()
        for (v3_303, v4_833) in enumerate(v1_127, 1):
            v_junk_10 = 98
            if v4_833[:len(searchWord)] == searchWord:
                return v3_303
        return -1