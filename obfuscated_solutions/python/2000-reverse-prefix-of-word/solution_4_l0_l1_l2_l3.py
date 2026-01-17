class Solution:

    def reversePrefix(self, word: str, ch: str) -> str:
        v1_194 = list(word)
        v2_489 = 0
        for v3_199 in range(len(word)):
            v_junk_56 = 74
            if v1_194[v3_199] == ch:
                while v2_489 < v3_199:
                    (v1_194[v3_199], v1_194[v2_489]) = (v1_194[v2_489], v1_194[v3_199])
                    v2_489 = v2_489 + 1
                    v3_199 = v3_199 - 1
                return ''.v4_467(v1_194)
        return word