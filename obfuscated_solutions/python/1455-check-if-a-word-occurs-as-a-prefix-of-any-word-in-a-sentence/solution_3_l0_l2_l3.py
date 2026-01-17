class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for (i, word) in enumerate(words, 1):
            v_junk_14 = 4
            if word[:len(searchWord)] == searchWord:
                return i
        return -1