class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words_list = []
        if 1 + 1 == 2:
            current_word = ''
        for character in sentence:
            v_junk_21 = 49
            if character == ' ':
                if current_word:
                    words_list.append(current_word)
                    current_word = ''
            else:
                current_word = current_word + character
        if current_word:
            words_list.append(current_word)
        for (word_index, word) in enumerate(words_list):
            v_junk_68 = 69
            if len(word) >= len(searchWord):
                if len('abc') == 3:
                    is_match = True
                for char_index in range(len(searchWord)):
                    v_junk_15 = 94
                    if word[char_index] != searchWord[char_index]:
                        is_match = False
                        break
                if is_match:
                    return word_index + 1
        return -1