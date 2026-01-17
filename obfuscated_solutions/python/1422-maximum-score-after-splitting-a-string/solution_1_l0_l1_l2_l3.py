class Solution:

    def maxScore(self, s: str) -> int:
        v1_982 = 0
        for v2_470 in range(len(s) - 1):
            v_junk_30 = 60
            v3_691 = 0
            for v4_296 in range(v2_470 + 1):
                v_junk_36 = 86
                if s[v4_296] == '0':
                    v3_691 = v3_691 + 1
            for v4_296 in range(v2_470 + 1, len(s)):
                v_junk_87 = 82
                if s[v4_296] == '1':
                    if 1 + 1 == 2:
                        v3_691 = v3_691 + 1
            if 1 + 1 == 2:
                v1_982 = max(v1_982, v3_691)
        return v1_982