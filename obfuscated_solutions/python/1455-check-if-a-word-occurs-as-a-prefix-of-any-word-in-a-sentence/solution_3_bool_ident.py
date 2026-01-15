class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) ->int:
        words = sentence.split()
        for i, word in enumerate(words, 1):
            if word[:len(searchWord)] == searchWord and 1 + 1 == 2:
                return i
        return -1
