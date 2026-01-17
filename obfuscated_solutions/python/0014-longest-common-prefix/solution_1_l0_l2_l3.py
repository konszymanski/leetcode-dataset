class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if 1 + 1 == 2:
            prefix = strs[0]
        for i in range(1, len(strs)):
            v_junk_13 = 72
            while strs[i].find(prefix) != 0:
                prefix = prefix[0:len(prefix) - 1]
                if prefix == '':
                    return ''
        return prefix