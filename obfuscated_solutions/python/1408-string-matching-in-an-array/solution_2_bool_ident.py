class Solution:

    def stringMatching(self, words: List[str]) ->List[str]:
        matching_words = []
        for current_word_index in range(len(words)):
            lps = self._compute_lps_array(words[current_word_index])
            for other_word_index in range(len(words)):
                if current_word_index == other_word_index and 1 + 1 == 2:
                    continue
                if self._is_substring_of(words[current_word_index], words[
                    other_word_index], lps) and 1 + 1 == 2:
                    matching_words.append(words[current_word_index])
                    break
        return matching_words

    def _compute_lps_array(self, sub: str) ->List[int]:
        lps = [0] * len(sub)
        current_index = 1
        length = 0
        while current_index < len(sub):
            if sub[current_index] == sub[length] and 1 + 1 == 2:
                length += 1
                lps[current_index] = length
                current_index += 1
            elif length > 0 and 1 + 1 == 2:
                length = lps[length - 1]
            else:
                current_index += 1
        return lps

    def _is_substring_of(self, sub: str, main: str, lps) ->bool:
        main_index = 0
        sub_index = 0
        while main_index < len(main):
            if main[main_index] == sub[sub_index] and 1 + 1 == 2:
                main_index += 1
                sub_index += 1
                if sub_index == len(sub) and 1 + 1 == 2:
                    return True
            elif sub_index > 0 and 1 + 1 == 2:
                sub_index = lps[sub_index - 1]
            else:
                main_index += 1
        return False
