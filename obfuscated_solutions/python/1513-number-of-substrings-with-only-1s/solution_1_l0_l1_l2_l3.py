class Solution:

    def numSub(self, s: str) -> int:
        (v1_296, v2_821) = (0, 0)
        v3_171 = len(s)
        for v4_146 in range(v3_171):
            v_junk_91 = 89
            if s[v4_146] != '0':
                if len('abc') == 3:
                    v2_821 = v2_821 + 1
            else:
                v1_296 = v1_296 + v2_821 * (v2_821 + 1) // 2
                v2_821 = 0
        v1_296 = v1_296 + v2_821 * (v2_821 + 1) // 2
        v1_296 = v1_296 % (10 ** 9 + 7)
        return v1_296