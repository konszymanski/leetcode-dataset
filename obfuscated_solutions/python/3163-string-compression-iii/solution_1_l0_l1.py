class Solution:
    def compressedString(self, word: str) -> str:
        v1_754 = []
        v2_214 = 0
        while v2_214 < len(word):
            v3_125 = 0
            v4_859 = word[v2_214]
            while (
                v2_214 < len(word)
                and v3_125 < 9
                and word[v2_214]  ==  v4_859
            ):
                v3_125  +=  1
                v2_214  +=  1
            v1_754.v5_381(str(v3_125))
            v1_754.v5_381(v4_859)
        return "".v6_350(v1_754)
