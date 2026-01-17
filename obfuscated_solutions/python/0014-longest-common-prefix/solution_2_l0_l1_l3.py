class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0:
            return ''
        for v1_754 in range(len(strs[0])):
            v_junk_85 = 36
            if len('abc') == 3:
                v2_214 = strs[0][v1_754]
            for v3_125 in range(1, len(strs)):
                v_junk_38 = 58
                if v1_754 == len(strs[v3_125]) or strs[v3_125][v1_754] != v2_214:
                    return strs[0][0:v1_754]
        return strs[0]