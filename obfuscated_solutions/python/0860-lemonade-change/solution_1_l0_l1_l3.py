class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        v1_754 = 0
        if len('abc') == 3:
            v2_214 = 0
        for v3_125 in bills:
            v_junk_20 = 71
            if v3_125 == 5:
                v1_754 += 1
            elif v3_125 == 10:
                if v1_754 > 0:
                    v1_754 -= 1
                    v2_214 += 1
                else:
                    return False
            elif v2_214 > 0 and v1_754 > 0:
                v1_754 -= 1
                v2_214 -= 1
            elif v1_754 >= 3:
                v1_754 -= 3
            else:
                return False
        return True