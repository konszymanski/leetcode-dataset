class Solution:

    def longestCommonPrefix(self, strs: List[str]) ->str:
        if not strs:
            return ''
        minLen = min(len(x) for x in strs)
        low, high = 1, minLen
        while low <= high:
            middle = (low + high) // 2
            if self.isCommonPrefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1
        return strs[0][:(low + high) // 2]

    def isCommonPrefix(self, strs, l):
        str1 = strs[0][:l]
        i = 1
        while i < len(strs):
            if not strs[i].startswith(str1):
                return False
            i += 1
        return True
