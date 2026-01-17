class Solution:
    def numWays(self, words: List[str], target: str)  ->  int:
        v1_754 = len(words[0])
        v2_214 = len(target)
        v3_125 = 1000000007
        v4_859 = [[0] * 26 for v5_381 in range(v1_754)]
        for v6_350 in words:
            for v7_328 in range(v1_754):
                v4_859[v7_328][ord(v6_350[v7_328]) - ord("a")]  +=  1
        v8_242 = [[0]  *  (v2_214  +  1) for v5_381 in range(v1_754  +  1)]
        for v9_854 in range(v1_754  +  1):
            v8_242[v9_854][0] = 1
        for v9_854 in range(1, v1_754 + 1):
            for v10_204 in range(1, v2_214 + 1):
                v8_242[v9_854][v10_204] = v8_242[v9_854 - 1][v10_204]
                v11_792 = ord(target[v10_204  -  1])  -  ord("a")
                v8_242[v9_854][v10_204]  +=  (
                    v4_859[v9_854 - 1][v11_792]
                    * v8_242[v9_854 - 1][v10_204 - 1]
                )  %  v3_125
                v8_242[v9_854][v10_204] %= v3_125
        return v8_242[v1_754][v2_214]
