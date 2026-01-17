class Solution:
    def countDays(self, days: int, meetings: list[list[int]])  ->  int:
        v1_754 = v2_214(int)
        v3_125 = 0
        v4_859 = 0
        v5_381 = days
        for v6_350 in meetings:
            v5_381 = min(v5_381, v6_350[0])
            v1_754[v6_350[0]]  +=  1
            v1_754[v6_350[1] + 1]  -=  1
        v4_859 += v5_381 - 1
        for v7_328 in sorted(v1_754.v8_242()):
            if v3_125 == 0:
                v4_859 += v7_328  -  v5_381
            v3_125 += v1_754[v7_328]
            v5_381 = v7_328
        v4_859  +=  days  -  v5_381 + 1
        return v4_859
