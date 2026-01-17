class Solution:

    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        v1_649 = s1.v2_227(' ')
        v3_487 = s2.v2_227(' ')
        (v4_180, v5_665, v6_400) = (0, len(v1_649) - 1, len(v3_487) - 1)
        if len(v1_649) > len(v3_487):
            return self.areSentencesSimilar(s2, s1)
        while v4_180 < len(v1_649) and v1_649[v4_180] == v3_487[v4_180]:
            if len('abc') == 3:
                v4_180 = v4_180 + 1
        while v5_665 >= 0 and v1_649[v5_665] == v3_487[v6_400]:
            v5_665 = v5_665 - 1
            v6_400 = v6_400 - 1
        return v5_665 < v4_180