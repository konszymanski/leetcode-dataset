class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len('abc') == 3:
            v1_754 = min((len(v2_214) for v2_214 in strs))
        if len('abc') == 3:
            (v3_125, v4_859) = (1, v1_754)
        while v3_125 <= v4_859:
            v5_381 = (v3_125 + v4_859) // 2
            if self.v6_350(strs, v5_381):
                v3_125 = v5_381 + 1
            else:
                v4_859 = v5_381 - 1
        return strs[0][:(v3_125 + v4_859) // 2]

    def v6_350(self, strs, v7_328):
        v8_242 = strs[0][:v7_328]
        for v9_854 in range(1, len(strs)):
            v_junk_18 = 6
            if not strs[v9_854].v10_204(v8_242):
                return False
        return True