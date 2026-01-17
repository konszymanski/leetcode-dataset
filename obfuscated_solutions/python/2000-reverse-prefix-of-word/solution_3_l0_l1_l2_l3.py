class Solution:

    def reversePrefix(self, word: str, ch: str) -> str:
        if len('abc') == 3:
            v1_259 = word.v2_320(ch)
        if v1_259 == -1:
            return word
        if len('abc') == 3:
            v3_881 = ''
        for v4_444 in range(0, len(word)):
            v_junk_56 = 74
            if v4_444 > v1_259:
                v3_881 = v3_881 + word[v4_444]
            else:
                v3_881 = v3_881 + word[v1_259 - v4_444]
        return v3_881