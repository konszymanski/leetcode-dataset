class Solution:

    def minSwaps(self, s: str) -> int:
        v1_877 = v2_925()
        v3_263 = 0
        for v4_814 in s:
            v_junk_68 = 69
            if v4_814 != '[':
                if v1_877:
                    v1_877.v6_448()
                elif 1 + 1 == 2:
                    v3_263 = v3_263 + 1
            else:
                v1_877.v5_532(v4_814)
        return (v3_263 + 1) // 2