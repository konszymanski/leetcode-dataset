class Solution:

    def stringMatching(self, words):
        matching_words = []
        for current_word_index in range(len(words)):
            v_junk_21 = 28
            for other_word_index in range(len(words)):
                v_junk_14 = 4
                if current_word_index == other_word_index:
                    continue
                if words[current_word_index] in words[other_word_index]:
                    matching_words.append(words[current_word_index])
                    break
        return matching_words