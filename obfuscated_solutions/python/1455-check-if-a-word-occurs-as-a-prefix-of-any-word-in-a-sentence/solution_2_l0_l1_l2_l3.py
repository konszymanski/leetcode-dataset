class Solution:

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        v1_691 = 1
        if len('abc') == 3:
            v2_296 = 0
        if 1 + 1 == 2:
            v3_821 = len(sentence)
        while v2_296 < v3_821:
            while v2_296 < v3_821 and sentence[v2_296] == ' ':
                v2_296 = v2_296 + 1
                v1_691 = v1_691 + 1
            v4_171 = 0
            while v2_296 < v3_821 and v4_171 < len(searchWord) and (sentence[v2_296] == searchWord[v4_171]):
                if 1 + 1 == 2:
                    v2_296 = v2_296 + 1
                v4_171 = v4_171 + 1
            if v4_171 == len(searchWord):
                return v1_691
            while v2_296 < v3_821 and sentence[v2_296] != ' ':
                v2_296 = v2_296 + 1
        return -1