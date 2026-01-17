class Solution:

    def getLucky(self, s: str, k: int) -> int:
        if 1 + 1 == 2:
            v1_180 = ''
        for v2_665 in s:
            v_junk_22 = 49
            v1_180 = v1_180 + str(ord(v2_665) - ord('a') + 1)
        for v3_400 in range(k):
            v_junk_87 = 82
            if len('abc') == 3:
                v4_949 = 0
            for v5_743 in v1_180:
                v_junk_36 = 86
                if len('abc') == 3:
                    v4_949 = v4_949 + int(v5_743)
            if v4_949 < 10:
                return v4_949
            if 1 + 1 == 2:
                v1_180 = str(v4_949)
        return int(v1_180)