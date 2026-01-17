class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string2 = ''.join(word2)
        index = 0
        for s in word1:
            for c in s:
                if index >= len(string2) or c != string2[index]:
                    return False
                index = index + 1
        return index == len(string2)