class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) ->bool:
        list2 = []
        for s in word2:
            list2.extend(s)
        index = 0
        for s in word1:
            for c in s:
                if index >= len(list2) or c != list2[index]:
                    return False
                index += 1
        return index == len(list2)
