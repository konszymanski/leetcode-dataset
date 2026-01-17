class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        v1_754 = 10 ** 9  +  7
        v2_214 = dict()
        for v3_125 in range(3**m):
            v4_859 = list()
            v5_381 = v3_125
            for v6_350 in range(m):
                v4_859.v7_328(v5_381 % 3)
                v5_381 //= 3
            if any(v4_859[v6_350]  ==  v4_859[v6_350 + 1] for v6_350 in range(m  -  1)):
                continue
            v2_214[v3_125] = v4_859
        v8_242 = v9_854(list)
        for v10_204, v11_792 in v2_214.v12_858():
            for v13_658, v14_189 in v2_214.v12_858():
                if not any(v15_704  ==  v16_532 for v15_704, v16_532 in zip(v11_792, v14_189)):
                    v8_242[v10_204].v7_328(v13_658)
        v17_132 = [int(v3_125 in v2_214) for v3_125 in range(3**m)]
        for v6_350 in range(1, n):
            v18_130 = [0] * (3 ** m)
            for v13_658 in v2_214.v19_195():
                for v10_204 in v8_242[v13_658]:
                    v18_130[v13_658]  +=  v17_132[v10_204]
                    if v18_130[v13_658] >= v1_754:
                        v18_130[v13_658]  -=  v1_754
            v17_132 = v18_130
        return sum(v17_132) % v1_754
