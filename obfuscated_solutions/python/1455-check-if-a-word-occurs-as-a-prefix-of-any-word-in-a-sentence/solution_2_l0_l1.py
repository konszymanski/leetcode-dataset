class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        v1_754 = 1
        v2_214 = 0
        v3_125 = len(sentence)
        while v2_214 < v3_125:
            while (
                v2_214 < v3_125
                and sentence[v2_214] == " "
            ):
                v2_214  +=  1
                v1_754  +=  1
            v4_859 = 0
            while (
                v2_214  <  v3_125
                and v4_859  <  len(searchWord)
                and sentence[v2_214]  ==  searchWord[v4_859]
            ):
                v2_214 += 1
                v4_859 += 1
            if v4_859 == len(searchWord):
                return v1_754
            while (
                v2_214 < v3_125
                and sentence[v2_214] != " "
            ):
                v2_214  +=  1
        return  - 1
