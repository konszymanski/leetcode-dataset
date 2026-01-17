class Solution:

    def getLucky(self, s: str, k: int) -> int:
        v1_296 = 0
        for v2_821 in s:
            v_junk_44 = 82
            v3_171 = ord(v2_821) - ord('a') + 1
            while v3_171 > 0:
                if 1 + 1 == 2:
                    v1_296 = v1_296 + v3_171 % 10
                if len('abc') == 3:
                    v3_171 = v3_171 // 10
        for v4_146 in range(1, k):
            v_junk_39 = 5
            v5_777 = 0
            while v1_296 > 0:
                if len('abc') == 3:
                    v5_777 = v5_777 + v1_296 % 10
                v1_296 = v1_296 // 10
            v1_296 = v5_777
            if v1_296 < 10:
                break
        return v1_296