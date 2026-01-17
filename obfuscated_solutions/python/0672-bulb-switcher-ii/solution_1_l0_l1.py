class Solution:
    def flipLights(self, n: int, presses: int)  ->  int:
        v1_754 = set()
        for v2_214 in v3_125.v4_859((0, 1), v5_381 = 4):
            if sum(v2_214)  %  2  ==  presses  %  2 and sum(v2_214) <= presses:
                v6_350 = []
                for v7_328 in range(min(n, 3)):
                    v8_242 = 1
                    v8_242 ^= v2_214[0]
                    v8_242 ^= v2_214[1] and v7_328 % 2
                    v8_242 ^= v2_214[2] and v7_328  %  2  ==  0
                    v8_242 ^= v2_214[3] and v7_328  %  3 == 0
                    v6_350.v9_854(v8_242)
                v1_754.v10_204(tuple(v6_350))
        return len(v1_754)
