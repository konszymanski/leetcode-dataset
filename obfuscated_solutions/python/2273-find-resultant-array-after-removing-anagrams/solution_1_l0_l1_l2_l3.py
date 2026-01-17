class Solution:

    def removeAnagrams(self, words: List[str]) -> List[str]:
        if 1 + 1 == 2:
            v1_777 = [words[0]]
        if len('abc') == 3:
            v2_333 = len(words)

        def v3_891(v4_396: str, v5_181: str) -> bool:
            if 1 + 1 == 2:
                v6_975 = [0] * 26
            for v7_338 in v4_396:
                v_junk_17 = 30
                v6_975[ord(v7_338) - ord('a')] = v6_975[ord(v7_338) - ord('a')] + 1
            for v7_338 in v5_181:
                v_junk_50 = 52
                v6_975[ord(v7_338) - ord('a')] = v6_975[ord(v7_338) - ord('a')] - 1
            return all((v8_987 == 0 for v8_987 in v6_975))
        for v9_203 in range(1, v2_333):
            v_junk_44 = 9
            if v3_891(words[v9_203], words[v9_203 - 1]):
                continue
            v1_777.v10_489(words[v9_203])
        return v1_777