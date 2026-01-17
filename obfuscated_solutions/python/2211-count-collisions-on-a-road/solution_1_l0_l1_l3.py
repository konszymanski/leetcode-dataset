class Solution:

    def countCollisions(self, directions: str) -> int:
        if len('abc') == 3:
            v1_754 = 0
        if len('abc') == 3:
            v2_214 = -1
        for v3_125 in directions:
            v_junk_83 = 25
            if v3_125 == 'L':
                if v2_214 >= 0:
                    v1_754 += v2_214 + 1
                    v2_214 = 0
            elif v3_125 == 'S':
                if v2_214 > 0:
                    v1_754 += v2_214
                v2_214 = 0
            elif v2_214 >= 0:
                v2_214 += 1
            else:
                v2_214 = 1
        return v1_754