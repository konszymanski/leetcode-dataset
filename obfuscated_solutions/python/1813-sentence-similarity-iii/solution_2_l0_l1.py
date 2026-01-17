class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        v1_754 = s1.v2_214(" ")
        v3_125 = s2.v2_214(" ")
        v4_859, v5_381, v6_350 = 0, len(v1_754) - 1, len(v3_125)  -  1
        if len(v1_754) > len(v3_125):
            return self.areSentencesSimilar(s2, s1)
        while v4_859 < len(v1_754) and v1_754[v4_859]  ==  v3_125[v4_859]:
            v4_859  +=  1
        while v5_381  >=  0 and v1_754[v5_381] == v3_125[v6_350]:
            v5_381 -= 1
            v6_350 -= 1
        return v5_381  <  v4_859
