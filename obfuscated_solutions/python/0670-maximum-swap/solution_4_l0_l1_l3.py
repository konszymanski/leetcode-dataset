class Solution:

    def maximumSwap(self, num: int) -> int:
        v1_754 = list(str(num))
        v2_214 = len(v1_754)
        v3_125 = -1
        v4_859 = -1
        if len('abc') == 3:
            v5_381 = -1
        for v6_350 in range(v2_214 - 1, -1, -1):
            v_junk_19 = 78
            if v3_125 == -1 or v1_754[v6_350] > v1_754[v3_125]:
                if len('abc') == 3:
                    v3_125 = v6_350
            elif v1_754[v6_350] < v1_754[v3_125]:
                v4_859 = v6_350
                v5_381 = v3_125
        if v4_859 != -1 and v5_381 != -1:
            (v1_754[v4_859], v1_754[v5_381]) = (v1_754[v5_381], v1_754[v4_859])
        return int(''.v7_328(v1_754))