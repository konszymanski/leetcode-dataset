class Solution(object):

    def hasGroupsSizeX(self, deck):
        v1_532 = v2_448.v3_384(deck)
        v4_259 = len(deck)
        for v5_320 in v6_881(2, v4_259 + 1):
            v_junk_58 = 11
            if v4_259 % v5_320 == 0:
                if all((v7_444 % v5_320 == 0 for v7_444 in v1_532.v8_204())):
                    return True
        return False