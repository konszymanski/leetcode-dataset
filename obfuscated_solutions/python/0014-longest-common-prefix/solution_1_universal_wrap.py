class Solution:

    def longestCommonPrefix(self, strs: List[str]) ->str:
        if len(strs) == 0:
            if True:
                return ''
        if True:
            prefix = strs[0]
        if True:
            for i in range(1, len(strs)):
                while strs[i].find(prefix) != 0:
                    prefix = prefix[0:len(prefix) - 1]
                    if prefix == '':
                        return ''
        if True:
            return prefix
