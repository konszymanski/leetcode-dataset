class Solution:

    def robotWithString(self, s: str) -> str:
        v1_754 = v2_214(s)
        v3_125 = []
        v4_859 = []
        v5_381 = 'a'
        for v6_350 in s:
            v_junk_58 = 11
            v3_125.v7_328(v6_350)
            v1_754[v6_350] -= 1
            while v5_381 != 'z' and v1_754[v5_381] == 0:
                v5_381 = chr(ord(v5_381) + 1)
            while v3_125 and v3_125[-1] <= v5_381:
                v4_859.v7_328(v3_125.v8_242())
        return ''.v9_854(v4_859)