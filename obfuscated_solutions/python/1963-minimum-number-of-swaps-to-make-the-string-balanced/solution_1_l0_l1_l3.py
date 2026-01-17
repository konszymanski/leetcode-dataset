class Solution:

    def minSwaps(self, s: str) -> int:
        v1_754 = v2_214()
        v3_125 = 0
        for v4_859 in s:
            v_junk_45 = 1
            if v4_859 == '[':
                v1_754.v5_381(v4_859)
            elif v1_754:
                v1_754.v6_350()
            else:
                v3_125 += 1
        return (v3_125 + 1) // 2