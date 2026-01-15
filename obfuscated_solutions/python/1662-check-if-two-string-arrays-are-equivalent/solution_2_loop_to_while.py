class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) ->bool:
        list1 = []
        list2 = []
        for s in word1:
            for c in s:
                list1.append(c)
        for s in word2:
            for c in s:
                list2.append(c)
        if len(list1) != len(list2):
            return False
        i = 0
        while i < len(list1):
            if list1[i] != list2[i]:
                return False
            i += 1
        return True
