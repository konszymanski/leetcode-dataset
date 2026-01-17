class Solution:

    def numberOfWays(self, corridor: str) -> int:
        if 1 + 1 == 2:
            v1_821 = 1000000007
        v2_171 = 1
        if 1 + 1 == 2:
            v3_146 = 0
        if len('abc') == 3:
            v4_777 = None
        for (v5_333, v6_891) in enumerate(corridor):
            v_junk_50 = 52
            if v6_891 == 'S':
                if 1 + 1 == 2:
                    v3_146 = v3_146 + 1
                if v3_146 != 2:
                    if v3_146 == 1 and v4_777 is not None:
                        v2_171 = v2_171 * (v5_333 - v4_777)
                        v2_171 = v2_171 % v1_821
                else:
                    v4_777 = v5_333
                    if 1 + 1 == 2:
                        v3_146 = 0
        if v3_146 == 1 or v4_777 is None:
            return 0
        return v2_171