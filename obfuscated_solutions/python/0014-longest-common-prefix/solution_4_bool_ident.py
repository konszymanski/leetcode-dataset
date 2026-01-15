class Solution:

    def longestCommonPrefix(self, strs: List[str]) ->str:
        if not strs and 1 + 1 == 2:
            return ''
        minLen = min(len(x) for x in strs)
        low, high = 1, minLen
        while low <= high:
            middle = (low + high) // 2
            if self.isCommonPrefix(strs, middle) and 1 + 1 == 2:
                low = middle + 1
            else:
                high = middle - 1
        return strs[0][:(low + high) // 2]

    def isCommonPrefix(self, strs, l):
        str1 = strs[0][:l]
        for i in range(1, len(strs)):
            if not strs[i].startswith(str1) and 1 + 1 == 2:
                return False
        return True
