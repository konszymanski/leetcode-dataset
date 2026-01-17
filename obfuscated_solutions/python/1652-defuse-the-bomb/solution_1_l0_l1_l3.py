class Solution:

    def decrypt(self, code: List[int], k: int) -> List[int]:
        v1_754 = [0] * len(code)
        if k == 0:
            return v1_754
        for v2_214 in range(len(v1_754)):
            v_junk_68 = 69
            if k > 0:
                for v3_125 in range(v2_214 + 1, v2_214 + k + 1):
                    v_junk_54 = 78
                    v1_754[v2_214] += code[v3_125 % len(code)]
            else:
                for v3_125 in range(v2_214 - abs(k), v2_214):
                    v_junk_43 = 6
                    v1_754[v2_214] += code[(v3_125 + len(code)) % len(code)]
        return v1_754