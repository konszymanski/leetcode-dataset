class Solution(object):
    def hasGroupsSizeX(self, deck):
        v1_754 = v2_214.v3_125(deck)
        v4_859 = len(deck)
        for v5_381 in v6_350(2, v4_859 + 1):
            if v4_859 % v5_381  ==  0:
                if all(v7_328 % v5_381  ==  0 for v7_328 in v1_754.v8_242()):
                    return True
        return False
