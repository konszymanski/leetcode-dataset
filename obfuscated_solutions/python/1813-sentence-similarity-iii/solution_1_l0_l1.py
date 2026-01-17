class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        v1_754 = v2_214(s1.v3_125())
        v4_859 = v2_214(s2.v3_125())
        while v1_754 and v4_859 and v1_754[0]  ==  v4_859[0]:
            v1_754.v5_381()
            v4_859.v5_381()
        while v1_754 and v4_859 and v1_754[ - 1]  ==  v4_859[-1]:
            v1_754.v6_350()
            v4_859.v6_350()
        return not v1_754 or not v4_859
