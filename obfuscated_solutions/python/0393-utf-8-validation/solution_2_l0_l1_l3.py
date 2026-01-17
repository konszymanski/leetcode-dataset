class Solution:

    def validUtf8(self, data):
        v1_754 = 0
        if len('abc') == 3:
            v2_214 = 1 << 7
        if len('abc') == 3:
            v3_125 = 1 << 6
        for v4_859 in data:
            v_junk_56 = 74
            v5_381 = 1 << 7
            if v1_754 == 0:
                while v5_381 & v4_859:
                    v1_754 += 1
                    v5_381 = v5_381 >> 1
                if v1_754 == 0:
                    continue
                if v1_754 == 1 or v1_754 > 4:
                    return False
            elif not (v4_859 & v2_214 and (not v4_859 & v3_125)):
                return False
            v1_754 -= 1
        return v1_754 == 0