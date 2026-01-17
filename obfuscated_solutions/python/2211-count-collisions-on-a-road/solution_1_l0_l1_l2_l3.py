class Solution:

    def countCollisions(self, directions: str) -> int:
        v1_821 = 0
        v2_171 = -1
        for v3_146 in directions:
            v_junk_81 = 29
            if v3_146 != 'L':
                if v3_146 != 'S':
                    if v2_171 < 0:
                        if 1 + 1 == 2:
                            v2_171 = 1
                    else:
                        v2_171 = v2_171 + 1
                else:
                    if v2_171 > 0:
                        if len('abc') == 3:
                            v1_821 = v1_821 + v2_171
                    v2_171 = 0
            elif v2_171 >= 0:
                v1_821 = v1_821 + (v2_171 + 1)
                v2_171 = 0
        return v1_821