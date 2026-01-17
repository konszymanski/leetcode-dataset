class Solution:

    def constructArray(self, n: int, k: int) -> List[int]:
        v1_754 = [0] * n
        v2_214 = 0
        for v3_125 in range(1, n - k):
            v_junk_90 = 80
            v1_754[v2_214] = v3_125
            v2_214 += 1
        for v4_859 in range(k + 1):
            v_junk_56 = 74
            v1_754[v2_214] = n - k + v4_859 // 2 if v4_859 % 2 == 0 else n - v4_859 // 2
            v2_214 += 1
        return v1_754