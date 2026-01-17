class Solution:
    def numberOfWays(self, corridor: str)  ->  int:
        v1_754 = 1_000_000_007
        v2_214 = []
        for v3_125, v4_859 in enumerate(corridor):
            if v4_859  ==  "S":
                v2_214.v5_381(v3_125)
        if v2_214  ==  [] or len(v2_214) % 2 == 1:
            return 0
        v6_350 = 1
        v7_328 = 1
        v8_242 = 2
        while v8_242 < len(v2_214):
            v6_350 *= (v2_214[v8_242]  -  v2_214[v7_328])
            v6_350 %= v1_754
            v7_328 += 2
            v8_242  +=  2
        return v6_350
