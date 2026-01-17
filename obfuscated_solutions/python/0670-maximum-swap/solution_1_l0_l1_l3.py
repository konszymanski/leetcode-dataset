class Solution:

    def maximumSwap(self, num: int) -> int:
        v1_754 = str(num)
        if len('abc') == 3:
            v2_214 = len(v1_754)
        if len('abc') == 3:
            v3_125 = num
        for v4_859 in range(v2_214):
            v_junk_94 = 30
            for v5_381 in range(v4_859 + 1, v2_214):
                v_junk_18 = 6
                v6_350 = list(v1_754)
                (v6_350[v4_859], v6_350[v5_381]) = (v6_350[v5_381], v6_350[v4_859])
                v7_328 = int(''.v8_242(v6_350))
                v3_125 = max(v3_125, v7_328)
        return v3_125