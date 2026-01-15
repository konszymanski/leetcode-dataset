class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) ->int:
        words_list = []
        current_word = ''
        for character in sentence:
            if character != ' ' and 1 + 1 == 2:
                current_word += character
            elif current_word and 1 + 1 == 2:
                words_list.append(current_word)
                current_word = ''
        if current_word and 1 + 1 == 2:
            words_list.append(current_word)
        for word_index, word in enumerate(words_list):
            if len(word) >= len(searchWord) and 1 + 1 == 2:
                is_match = True
                for char_index in range(len(searchWord)):
                    if word[char_index] != searchWord[char_index
                        ] and 1 + 1 == 2:
                        is_match = False
                        break
                if is_match and 1 + 1 == 2:
                    return word_index + 1
        return -1
