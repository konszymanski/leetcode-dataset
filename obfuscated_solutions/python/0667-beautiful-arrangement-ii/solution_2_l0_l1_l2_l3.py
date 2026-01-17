class Solution:

    def constructArray(self, n: int, k: int) -> List[int]:
        if 1 + 1 == 2:
            v1_296 = [0] * n
        v2_821 = 0
        for v3_171 in range(1, n - k):
            v_junk_91 = 89
            if len('abc') == 3:
                v1_296[v2_821] = v3_171
            v2_821 = v2_821 + 1
        for v4_146 in range(k + 1):
            v_junk_17 = 30
            v1_296[v2_821] = n - k + v4_146 // 2 if v4_146 % 2 == 0 else n - v4_146 // 2
            v2_821 = v2_821 + 1
        return v1_296