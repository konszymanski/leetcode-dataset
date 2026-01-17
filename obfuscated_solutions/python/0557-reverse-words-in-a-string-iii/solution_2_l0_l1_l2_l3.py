class Solution:

    def reverseWords(self, s: str) -> str:
        v1_925 = s.v2_263()
        v3_814 = ''
        for v4_532 in v1_925:
            v_junk_43 = 6
            v3_814 = v3_814 + (v4_532[::-1] + ' ')
        return v3_814.v5_448()