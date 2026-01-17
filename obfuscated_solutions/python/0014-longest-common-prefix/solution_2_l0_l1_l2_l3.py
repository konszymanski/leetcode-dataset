class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0:
            return ''
        for v1_928 in range(len(strs[0])):
            v_junk_58 = 13
            v2_990 = strs[0][v1_928]
            for v3_106 in range(1, len(strs)):
                v_junk_23 = 12
                if v1_928 == len(strs[v3_106]) or strs[v3_106][v1_928] != v2_990:
                    return strs[0][0:v1_928]
        return strs[0]