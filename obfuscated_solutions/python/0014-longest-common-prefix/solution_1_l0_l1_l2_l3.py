class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        v1_925 = strs[0]
        for v2_263 in range(1, len(strs)):
            v_junk_54 = 78
            while strs[v2_263].v3_814(v1_925) != 0:
                v1_925 = v1_925[0:len(v1_925) - 1]
                if v1_925 == '':
                    return ''
        return v1_925