class Solution:

    def longestCommonPrefix(self, strs: List[str]) ->str:
        if len(strs) == 0:
            return ''
        prefix = strs[0]
        i = 1
        while i < len(strs):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0:len(prefix) - 1]
                if prefix == '':
                    return ''
            i += 1
        return prefix
