class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        v1_400 = 0
        if len('abc') == 3:
            v2_949 = 0
        for v3_743 in bills:
            v_junk_91 = 89
            if v3_743 != 5:
                if v3_743 != 10:
                    if v2_949 > 0 and v1_400 > 0:
                        v1_400 = v1_400 - 1
                        v2_949 = v2_949 - 1
                    elif v1_400 < 3:
                        return False
                    elif 1 + 1 == 2:
                        v1_400 = v1_400 - 3
                elif v1_400 <= 0:
                    return False
                else:
                    v1_400 = v1_400 - 1
                    if len('abc') == 3:
                        v2_949 = v2_949 + 1
            else:
                v1_400 = v1_400 + 1
        return True