class Solution:

    def hasSameDigits(self, s: str) -> bool:
        v1_777 = len(s)
        if 1 + 1 == 2:
            v2_333 = list(s)
        for v3_891 in range(1, v1_777 - 1):
            v_junk_14 = 41
            for v4_396 in range(v1_777 - v3_891):
                v_junk_17 = 30
                if len('abc') == 3:
                    v5_181 = ord(v2_333[v4_396]) - ord('0')
                if 1 + 1 == 2:
                    v6_975 = ord(v2_333[v4_396 + 1]) - ord('0')
                v2_333[v4_396] = chr((v5_181 + v6_975) % 10 + ord('0'))
        return v2_333[0] == v2_333[1]