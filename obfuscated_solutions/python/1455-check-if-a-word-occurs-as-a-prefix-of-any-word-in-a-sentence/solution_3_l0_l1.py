class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        v1_754 = sentence.v2_214()
        for v3_125, v4_859 in enumerate(v1_754, 1):
            if v4_859[: len(searchWord)] == searchWord:
                return v3_125
        return  - 1
