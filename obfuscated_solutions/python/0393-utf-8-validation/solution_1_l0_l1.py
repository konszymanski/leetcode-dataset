class Solution:
    def v1_754(self, v2_214):
        v3_125 = 0
        for v4_859 in v2_214:
            v5_381 = format(v4_859, '
            if v3_125 == 0:
                for v6_350 in v5_381:
                    if v6_350  ==  '0': break
                    v3_125  +=  1
                if v3_125  ==  0:
                    continue
                if v3_125 == 1 or v3_125 > 4:
                    return False
            else:
                if not (v5_381[0] == '1' and v5_381[1] == '0'):
                    return False
            v3_125 -= 1
        return v3_125  ==  0
