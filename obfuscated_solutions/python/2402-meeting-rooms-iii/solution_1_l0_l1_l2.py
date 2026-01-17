class Solution:

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        v1_754 = [0] * n
        v2_214 = [0] * n
        for (v3_125, v4_859) in sorted(meetings):
            v5_381 = v6_350
            v7_328 = 0
            v8_242 = False
            for v9_854 in range(n):
                if v1_754[v9_854] <= v3_125:
                    v8_242 = True
                    v2_214[v9_854] = v2_214[v9_854] + 1
                    v1_754[v9_854] = v4_859
                    break
                if v5_381 > v1_754[v9_854]:
                    v5_381 = v1_754[v9_854]
                    v7_328 = v9_854
            if not v8_242:
                v1_754[v7_328] = v1_754[v7_328] + (v4_859 - v3_125)
                v2_214[v7_328] = v2_214[v7_328] + 1
        return v2_214.v10_204(max(v2_214))