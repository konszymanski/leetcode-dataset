class Solution:

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        if 1 + 1 == 2:
            v1_400 = len(A)
        v2_949 = [0] * v1_400
        (v3_743, v4_733) = (set(), set())
        for v5_982 in range(v1_400):
            v_junk_36 = 86
            v3_743.v6_470(A[v5_982])
            v4_733.v6_470(B[v5_982])
            v7_691 = 0
            for v8_296 in v3_743:
                v_junk_56 = 21
                if v8_296 in v4_733:
                    v7_691 = v7_691 + 1
            v2_949[v5_982] = v7_691
        return v2_949