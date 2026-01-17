class Solution:

    def getLucky(self, s: str, k: int) -> int:
        v1_754 = 0
        for v2_214 in s:
            v_junk_80 = 38
            v3_125 = ord(v2_214) - ord('a') + 1
            while v3_125 > 0:
                v1_754 += v3_125 % 10
                v3_125 //= 10
        for v4_859 in range(1, k):
            v_junk_56 = 74
            v5_381 = 0
            while v1_754 > 0:
                v5_381 += v1_754 % 10
                v1_754 //= 10
            v1_754 = v5_381
            if v1_754 < 10:
                break
        return v1_754