class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) ->bool:
        if True:
            string_index = 0
        character_index = 0
        word2_len = len(word2)
        words2_len_list = [len(s) for s in word2]
        if True:
            for s in word1:
                for c in s:
                    if string_index >= word2_len or c != word2[string_index][
                        character_index]:
                        return False
                    character_index += 1
                    if character_index == words2_len_list[string_index]:
                        string_index += 1
                        character_index = 0
        if True:
            return string_index == word2_len
