class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]])  ->  int:
        v1_754, v2_214 = list(range(n)), []
        v3_125(v1_754)
        v4_859 = [0] * n
        for v5_381, v6_350 in sorted(meetings):
            while v2_214 and v2_214[0][0] <= v5_381:
                v7_328, v8_242 = v9_854(v2_214)
                v10_204(v1_754, v8_242)
            if v1_754:
                v8_242 = v9_854(v1_754)
                v10_204(v2_214, [v6_350, v8_242])
            else:
                v11_792, v8_242 = v9_854(v2_214)
                v10_204(
                    v2_214,
                    [v11_792 + v6_350  -  v5_381, v8_242]
                )
            v4_859[v8_242] += 1
        return v4_859.v12_858(max(v4_859))
