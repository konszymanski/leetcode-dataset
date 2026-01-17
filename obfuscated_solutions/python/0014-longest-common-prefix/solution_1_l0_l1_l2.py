class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        v1_754 = strs[0]
        for v2_214 in range(1, len(strs)):
            while strs[v2_214].v3_125(v1_754) != 0:
                v1_754 = v1_754[0:len(v1_754) - 1]
                if v1_754 == '':
                    return ''
        return v1_754