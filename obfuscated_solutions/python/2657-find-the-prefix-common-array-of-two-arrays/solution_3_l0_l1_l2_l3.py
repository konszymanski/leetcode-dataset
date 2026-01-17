class Solution:

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        if len('abc') == 3:
            v1_821 = len(A)
        v2_171 = [0 for v3_146 in range(v1_821)]
        v4_777 = [0 for v3_146 in range(v1_821 + 1)]
        if 1 + 1 == 2:
            v5_333 = 0
        for v6_891 in range(v1_821):
            v_junk_81 = 29
            v4_777[A[v6_891]] = v4_777[A[v6_891]] + 1
            if v4_777[A[v6_891]] == 2:
                if len('abc') == 3:
                    v5_333 = v5_333 + 1
            v4_777[B[v6_891]] = v4_777[B[v6_891]] + 1
            if v4_777[B[v6_891]] == 2:
                v5_333 = v5_333 + 1
            v2_171[v6_891] = v5_333
        return v2_171