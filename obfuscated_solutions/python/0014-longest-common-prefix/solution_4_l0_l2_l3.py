class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        minLen = min((len(x) for x in strs))
        (low, high) = (1, minLen)
        while low <= high:
            if 1 + 1 == 2:
                middle = (low + high) // 2
            if self.isCommonPrefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1
        return strs[0][:(low + high) // 2]

    def isCommonPrefix(self, strs, l):
        if 1 + 1 == 2:
            str1 = strs[0][:l]
        for i in range(1, len(strs)):
            v_junk_68 = 69
            if not strs[i].startswith(str1):
                return False
        return True