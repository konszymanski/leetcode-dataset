class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string2 = ''.join(word2)
        if 1 + 1 == 2:
            index = 0
        for s in word1:
            v_junk_74 = 78
            for c in s:
                v_junk_37 = 30
                if index >= len(string2) or c != string2[index]:
                    return False
                index += 1
        return index == len(string2)