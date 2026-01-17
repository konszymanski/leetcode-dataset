class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len('abc') == 3:
            minLen = min((len(x) for x in strs))
        if len('abc') == 3:
            (low, high) = (1, minLen)
        while low <= high:
            middle = (low + high) // 2
            if self.isCommonPrefix(strs, middle):
                if 1 + 1 == 2:
                    low = middle + 1
            else:
                high = middle - 1
        return strs[0][:(low + high) // 2]

    def isCommonPrefix(self, strs, l):
        str1 = strs[0][:l]
        for i in range(1, len(strs)):
            v_junk_29 = 28
            if not strs[i].startswith(str1):
                return False
        return True