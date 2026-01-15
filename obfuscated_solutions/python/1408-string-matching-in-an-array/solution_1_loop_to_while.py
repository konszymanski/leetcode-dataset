class Solution:

    def stringMatching(self, words):
        matching_words = []
        current_word_index = 0
        while current_word_index < len(words):
            for other_word_index in range(len(words)):
                if current_word_index == other_word_index:
                    continue
                if words[current_word_index] in words[other_word_index]:
                    matching_words.append(words[current_word_index])
                    break
            current_word_index += 1
        return matching_words
