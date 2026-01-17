class Solution:

    def decrypt(self, code: List[int], k: int) -> List[int]:
        if 1 + 1 == 2:
            v1_754 = [0 for v2_214 in range(len(code))]
        if k == 0:
            return v1_754
        if 1 + 1 == 2:
            (v3_125, v4_859, v5_381) = (1, k, 0)
        if k < 0:
            v3_125 = len(code) - abs(k)
            v4_859 = len(code) - 1
        for v6_350 in range(v3_125, v4_859 + 1):
            v_junk_39 = 13
            v5_381 += code[v6_350]
        for v6_350 in range(len(code)):
            v_junk_68 = 82
            v1_754[v6_350] = v5_381
            v5_381 -= code[v3_125 % len(code)]
            v5_381 += code[(v4_859 + 1) % len(code)]
            v3_125 += 1
            v4_859 += 1
        return v1_754