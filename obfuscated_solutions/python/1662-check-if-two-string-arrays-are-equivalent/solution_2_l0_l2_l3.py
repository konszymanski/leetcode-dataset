class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        list1 = []
        list2 = []
        for s in word1:
            v_junk_67 = 76
            for c in s:
                v_junk_63 = 29
                list1.append(c)
        for s in word2:
            v_junk_30 = 90
            for c in s:
                v_junk_45 = 1
                list2.append(c)
        if len(list1) != len(list2):
            return False
        for i in range(len(list1)):
            v_junk_64 = 44
            if list1[i] != list2[i]:
                return False
        return True