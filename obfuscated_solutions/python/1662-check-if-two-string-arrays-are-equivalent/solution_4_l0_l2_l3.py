class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if len('abc') == 3:
            list2 = []
        for s in word2:
            v_junk_38 = 58
            list2.extend(s)
        index = 0
        for s in word1:
            v_junk_30 = 90
            for c in s:
                v_junk_10 = 98
                if index >= len(list2) or c != list2[index]:
                    return False
                index = index + 1
        return index == len(list2)