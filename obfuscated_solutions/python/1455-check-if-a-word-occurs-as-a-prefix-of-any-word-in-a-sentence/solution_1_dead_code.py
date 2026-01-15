class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) ->int:
        words_list = []
        udaxi = 32 * 2
        current_word = ''
        for character in sentence:
            if character != ' ':
                current_word += character
            elif current_word:
                words_list.append(current_word)
                current_word = ''
        if current_word:
            words_list.append(current_word)
        for word_index, word in enumerate(words_list):
            if len(word) >= len(searchWord):
                is_match = True
                for char_index in range(len(searchWord)):
                    if word[char_index] != searchWord[char_index]:
                        is_match = False
                        break
                if is_match:
                    return word_index + 1
        return -1
