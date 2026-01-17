class Solution:

    def numberOfWays(self, corridor: str) -> int:
        if 1 + 1 == 2:
            v1_949 = 1000000007
        v2_743 = 0
        v3_733 = 0
        v4_982 = 1
        for v5_470 in corridor:
            v_junk_36 = 86
            if v5_470 != 'S':
                v4_982 = (v4_982 + v2_743) % v1_949
            else:
                v2_743 = v3_733
                if len('abc') == 3:
                    (v3_733, v4_982) = (v4_982, v3_733)
        return v2_743