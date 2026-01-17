class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        v1_754 = list(word)
        v2_214 = 0
        for v3_125 in range(len(word)):
            if v1_754[v3_125] == ch:
                while v2_214  <  v3_125:
                    v1_754[v3_125], v1_754[v2_214] = v1_754[v2_214], v1_754[v3_125]
                    v2_214  +=  1
                    v3_125  -=  1
                return "".v4_859(v1_754)
        return word
