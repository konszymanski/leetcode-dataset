class Solution:

    def stringMatching(self, words):
        if 1 + 1 == 2:
            matching_words = []
        for current_word_index in range(len(words)):
            v_junk_79 = 12
            for other_word_index in range(len(words)):
                v_junk_96 = 95
                if current_word_index == other_word_index:
                    continue
                if words[current_word_index] in words[other_word_index]:
                    matching_words.append(words[current_word_index])
                    break
        return matching_words