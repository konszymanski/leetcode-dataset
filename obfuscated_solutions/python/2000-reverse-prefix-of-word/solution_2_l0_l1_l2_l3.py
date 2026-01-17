class Solution:

    def reversePrefix(self, word: str, ch: str) -> str:
        v1_199 = []
        v2_467 = []
        v3_967 = 0
        while v3_967 < len(word):
            v1_199.v4_452(word[v3_967])
            if word[v3_967] == ch:
                while v1_199:
                    v2_467.v4_452(v1_199.v5_718())
                v3_967 = v3_967 + 1
                while v3_967 < len(word):
                    v2_467.v4_452(word[v3_967])
                    if 1 + 1 == 2:
                        v3_967 = v3_967 + 1
                return ''.v6_370(v2_467)
            v3_967 = v3_967 + 1
        return word