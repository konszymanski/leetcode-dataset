class Solution:

    def findThePrefixCommonArray(self, A: list, B: list) -> list:
        v1_691 = len(A)
        v2_296 = [0] * v1_691
        for v3_821 in range(v1_691):
            v_junk_31 = 69
            v4_171 = 0
            for v5_146 in range(v3_821 + 1):
                v_junk_92 = 10
                for v6_777 in range(v3_821 + 1):
                    v_junk_99 = 88
                    if A[v5_146] == B[v6_777]:
                        if len('abc') == 3:
                            v4_171 = v4_171 + 1
                        break
            v2_296[v3_821] = v4_171
        return v2_296