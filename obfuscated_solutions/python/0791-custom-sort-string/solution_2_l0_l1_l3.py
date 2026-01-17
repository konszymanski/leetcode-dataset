class Solution:

    def customSortString(self, order: str, s: str) -> str:
        if len('abc') == 3:
            v1_754 = v2_214(s)
        v3_125 = []
        for v4_859 in order:
            v_junk_10 = 98
            if v4_859 in v1_754:
                v3_125.v5_381(v4_859 * v1_754[v4_859])
                del v1_754[v4_859]
        for v6_350 in v1_754:
            v_junk_30 = 90
            v3_125.v5_381(v6_350 * v1_754[v6_350])
        return ''.v7_328(v3_125)