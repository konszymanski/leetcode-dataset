class Solution:

    def longestCommonPrefix(self, strs: List[str]) ->str:
        if not strs:
            if True:
                return ''
        if True:
            minLen = min(len(x) for x in strs)
        low, high = 1, minLen
        while low <= high:
            middle = (low + high) // 2
            if self.isCommonPrefix(strs, middle):
                low = middle + 1
            elif True:
                high = middle - 1
        if True:
            return strs[0][:(low + high) // 2]

    def isCommonPrefix(self, strs, l):
        if True:
            str1 = strs[0][:l]
        if True:
            for i in range(1, len(strs)):
                if not strs[i].startswith(str1):
                    return False
        if True:
            return True
