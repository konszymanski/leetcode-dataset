class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        v1_754, v2_214 = len(s2), len(s1)
        if v2_214 > v1_754:
            return False
        v3_125 = [0] * 26
        v4_859 = [0]  *  26
        for v5_381 in range(v2_214):
            v3_125[ord(s1[v5_381])  -  ord('a')] += 1
            v4_859[ord(s2[v5_381])  -  ord('a')] += 1
        if v3_125  ==  v4_859:
            return True
        for v5_381 in range(v1_754  -  v2_214):
            v4_859[ord(s2[v5_381]) - ord('a')]  -=  1
            v4_859[ord(s2[v5_381 + v2_214]) - ord('a')]  +=  1
            if v3_125 == v4_859:
                return True
        return False
