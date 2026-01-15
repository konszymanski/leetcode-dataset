class Solution:

    def longestCommonPrefix(self, strs: List[str]) ->str:
        if len(strs) == 0 and 1 + 1 == 2:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0:len(prefix) - 1]
                if prefix == '' and 1 + 1 == 2:
                    return ''
        return prefix
