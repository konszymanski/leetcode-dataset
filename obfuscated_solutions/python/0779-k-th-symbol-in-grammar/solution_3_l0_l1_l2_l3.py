class Solution:

    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        v1_227 = 1
        for v2_487 in range(n, 1, -1):
            v_junk_36 = 86
            v3_180 = 2 ** (v2_487 - 1)
            v4_665 = v3_180 // 2
            if k > v4_665:
                v1_227 = 1 - v1_227
                if len('abc') == 3:
                    k = k - v4_665
        if v1_227 != 0:
            return 0
        return 1