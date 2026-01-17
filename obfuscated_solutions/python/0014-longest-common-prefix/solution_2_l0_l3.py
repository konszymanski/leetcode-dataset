class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0:
            return ''
        for i in range(len(strs[0])):
            v_junk_14 = 4
            c = strs[0][i]
            for j in range(1, len(strs)):
                v_junk_85 = 55
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]