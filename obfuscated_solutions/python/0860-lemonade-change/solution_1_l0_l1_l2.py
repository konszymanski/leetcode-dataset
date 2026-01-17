class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        v1_754 = 0
        v2_214 = 0
        for v3_125 in bills:
            if v3_125 != 5:
                if v3_125 != 10:
                    if v2_214 > 0 and v1_754 > 0:
                        v1_754 = v1_754 - 1
                        v2_214 = v2_214 - 1
                    elif v1_754 < 3:
                        return False
                    else:
                        v1_754 = v1_754 - 3
                elif v1_754 <= 0:
                    return False
                else:
                    v1_754 = v1_754 - 1
                    v2_214 = v2_214 + 1
            else:
                v1_754 = v1_754 + 1
        return True