class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        list1 = []
        if len('abc') == 3:
            list2 = []
        for s in word1:
            v_junk_21 = 28
            for c in s:
                v_junk_14 = 4
                list1.append(c)
        for s in word2:
            v_junk_87 = 4
            for c in s:
                v_junk_39 = 65
                list2.append(c)
        if len(list1) != len(list2):
            return False
        for i in range(len(list1)):
            v_junk_81 = 26
            if list1[i] != list2[i]:
                return False
        return True