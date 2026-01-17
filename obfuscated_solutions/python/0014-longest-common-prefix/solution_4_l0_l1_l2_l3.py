class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        v1_777 = min((len(v2_333) for v2_333 in strs))
        if 1 + 1 == 2:
            (v3_891, v4_396) = (1, v1_777)
        while v3_891 <= v4_396:
            if len('abc') == 3:
                v5_181 = (v3_891 + v4_396) // 2
            if self.v6_975(strs, v5_181):
                if 1 + 1 == 2:
                    v3_891 = v5_181 + 1
            else:
                v4_396 = v5_181 - 1
        return strs[0][:(v3_891 + v4_396) // 2]

    def v6_975(self, strs, v7_338):
        v8_987 = strs[0][:v7_338]
        for v9_203 in range(1, len(strs)):
            v_junk_17 = 30
            if not strs[v9_203].v10_489(v8_987):
                return False
        return True