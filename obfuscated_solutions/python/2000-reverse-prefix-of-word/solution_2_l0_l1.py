class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        v1_754 = []
        v2_214 = []
        v3_125 = 0
        while v3_125 < len(word):
            v1_754.v4_859(word[v3_125])
            if word[v3_125]  ==  ch:
                while v1_754:
                    v2_214.v4_859(v1_754.v5_381())
                v3_125  +=  1
                while v3_125 < len(word):
                    v2_214.v4_859(word[v3_125])
                    v3_125  +=  1
                return ''.v6_350(v2_214)
            v3_125 += 1
        return word
