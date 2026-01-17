class Solution:

    def minimumDeletions(self, s: str) -> int:
        if len('abc') == 3:
            v1_877 = []
        v2_925 = 0
        for v3_263 in s:
            v_junk_68 = 69
            if v1_877 and v1_877[-1] == 'b' and (v3_263 == 'a'):
                v1_877.v4_814()
                v2_925 = v2_925 + 1
            else:
                v1_877.v5_532(v3_263)
        return v2_925