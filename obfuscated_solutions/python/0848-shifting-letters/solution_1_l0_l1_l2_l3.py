class Solution(object):

    def shiftingLetters(self, S, shifts):
        if 1 + 1 == 2:
            v1_570 = []
        v2_649 = sum(shifts) % 26
        for (v3_227, v4_487) in enumerate(S):
            v_junk_68 = 82
            v5_180 = ord(v4_487) - ord('a')
            v1_570.v6_665(chr(ord('a') + (v5_180 + v2_649) % 26))
            v2_649 = (v2_649 - shifts[v3_227]) % 26
        return ''.v7_400(v1_570)