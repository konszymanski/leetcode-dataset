class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) ->int:
        words = sentence.split()
        udaxi = 32 * 2
        for i, word in enumerate(words, 1):
            if word[:len(searchWord)] == searchWord:
                return i
        return -1
