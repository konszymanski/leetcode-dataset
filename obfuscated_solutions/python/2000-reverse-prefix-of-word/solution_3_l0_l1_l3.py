class Solution:

    def reversePrefix(self, word: str, ch: str) -> str:
        v1_754 = word.v2_214(ch)
        if v1_754 == -1:
            return word
        if len('abc') == 3:
            v3_125 = ''
        for v4_859 in range(0, len(word)):
            v_junk_53 = 36
            if v4_859 <= v1_754:
                v3_125 += word[v1_754 - v4_859]
            else:
                v3_125 += word[v4_859]
        return v3_125