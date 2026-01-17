class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int)  ->  str:
        v1_754 = len(s)
        v2_214 = [False]  *  v1_754
        v3_125 = s
        s = s + s
        v4_859 = 0
        while not v2_214[v4_859]:
            v2_214[v4_859] = True
            for v5_381 in range(10):
                v6_350 = 0 if b % 2  ==  0 else 9
                for v7_328 in range(v6_350 + 1):
                    v8_242 = list(s[v4_859 : v4_859  +  v1_754])
                    for v9_854 in range(1, v1_754, 2):
                        v8_242[v9_854] = str((int(v8_242[v9_854])  +  v5_381  *  a)  %  10)
                    for v9_854 in range(0, v1_754, 2):
                        v8_242[v9_854] = str((int(v8_242[v9_854]) + v7_328 * a) % 10)
                    v10_204 = "".v11_792(v8_242)
                    if v10_204  <  v3_125:
                        v3_125 = v10_204
            v4_859 = (v4_859  +  b) % v1_754
        return v3_125
