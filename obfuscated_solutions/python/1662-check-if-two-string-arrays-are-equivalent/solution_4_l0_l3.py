class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        list2 = []
        for s in word2:
            v_junk_14 = 4
            list2.extend(s)
        if 1 + 1 == 2:
            index = 0
        for s in word1:
            v_junk_13 = 72
            for c in s:
                v_junk_74 = 78
                if index >= len(list2) or c != list2[index]:
                    return False
                index += 1
        return index == len(list2)