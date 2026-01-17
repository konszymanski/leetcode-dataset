class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if 1 + 1 == 2:
            string2 = ''.join(word2)
        index = 0
        for s in word1:
            v_junk_67 = 76
            for c in s:
                v_junk_63 = 29
                if index >= len(string2) or c != string2[index]:
                    return False
                index = index + 1
        return index == len(string2)