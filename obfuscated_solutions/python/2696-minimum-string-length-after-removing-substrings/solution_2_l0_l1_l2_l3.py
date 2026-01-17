class Solution:

    def minLength(self, s: str) -> int:
        v1_529 = []
        for v2_325 in s:
            v_junk_23 = 12
            if not v1_529:
                v1_529.v3_559(v2_325)
                continue
            if v2_325 == 'B' and v1_529[-1] == 'A':
                v1_529.v4_703()
            elif v2_325 == 'D' and v1_529[-1] == 'C':
                v1_529.v4_703()
            else:
                v1_529.v3_559(v2_325)
        return len(v1_529)