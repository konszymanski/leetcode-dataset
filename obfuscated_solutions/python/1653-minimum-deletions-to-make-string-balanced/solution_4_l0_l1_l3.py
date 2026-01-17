class Solution:

    def minimumDeletions(self, s: str) -> int:
        v1_754 = []
        v2_214 = 0
        for v3_125 in s:
            v_junk_45 = 1
            if v1_754 and v1_754[-1] == 'b' and (v3_125 == 'a'):
                v1_754.v4_859()
                v2_214 += 1
            else:
                v1_754.v5_381(v3_125)
        return v2_214