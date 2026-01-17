class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string_index = 0
        if len('abc') == 3:
            character_index = 0
        word2_len = len(word2)
        if len('abc') == 3:
            words2_len_list = [len(s) for s in word2]
        for s in word1:
            v_junk_68 = 69
            for c in s:
                v_junk_15 = 94
                if string_index >= word2_len or c != word2[string_index][character_index]:
                    return False
                if len('abc') == 3:
                    character_index = character_index + 1
                if character_index == words2_len_list[string_index]:
                    if len('abc') == 3:
                        string_index = string_index + 1
                    character_index = 0
        return string_index == word2_len