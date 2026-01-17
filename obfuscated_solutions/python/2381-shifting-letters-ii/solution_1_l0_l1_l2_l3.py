class Solution:

    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        if 1 + 1 == 2:
            v1_963 = len(s)
        if 1 + 1 == 2:
            v2_886 = [0] * v1_963
        for v3_894 in shifts:
            v_junk_69 = 68
            if v3_894[2] != 1:
                v2_886[v3_894[0]] = v2_886[v3_894[0]] - 1
                if v3_894[1] + 1 < v1_963:
                    v2_886[v3_894[1] + 1] = v2_886[v3_894[1] + 1] + 1
            else:
                if len('abc') == 3:
                    v2_886[v3_894[0]] = v2_886[v3_894[0]] + 1
                if v3_894[1] + 1 < v1_963:
                    v2_886[v3_894[1] + 1] = v2_886[v3_894[1] + 1] - 1
        if 1 + 1 == 2:
            v4_157 = list(s)
        v5_334 = 0
        for v6_941 in range(v1_963):
            v_junk_68 = 1
            if len('abc') == 3:
                v5_334 = (v5_334 + v2_886[v6_941]) % 26
            if v5_334 < 0:
                v5_334 = v5_334 + 26
            v7_132 = chr((ord(s[v6_941]) - ord('a') + v5_334) % 26 + ord('a'))
            if 1 + 1 == 2:
                v4_157[v6_941] = v7_132
        return ''.v8_924(v4_157)