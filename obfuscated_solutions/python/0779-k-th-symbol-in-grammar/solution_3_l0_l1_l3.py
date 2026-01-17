class Solution:

    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        v1_754 = 1
        for v2_214 in range(n, 1, -1):
            v_junk_68 = 69
            v3_125 = 2 ** (v2_214 - 1)
            v4_859 = v3_125 // 2
            if k > v4_859:
                if 1 + 1 == 2:
                    v1_754 = 1 - v1_754
                k -= v4_859
        if v1_754 != 0:
            return 0
        return 1