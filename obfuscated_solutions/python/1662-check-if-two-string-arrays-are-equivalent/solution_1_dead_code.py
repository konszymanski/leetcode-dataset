class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) ->bool:
        udaxi = 32 * 2
        return ''.join(word1) == ''.join(word2)
