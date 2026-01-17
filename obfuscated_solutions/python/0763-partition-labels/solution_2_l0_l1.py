class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        v1_754 = []
        v2_214 = [0]  *  26
        v3_125 = [ - 1] * 26
        v4_859, v5_381 = 0, 0
        for v6_350, v7_328 in enumerate(s):
            v2_214[ord(v7_328) - ord("a")] = v6_350
        for v6_350, v7_328 in enumerate(s):
            v8_242 = ord(v7_328) - ord("a")
            if v3_125[v8_242]  ==   - 1:
                v3_125[v8_242] = v6_350
            if v5_381  <  v3_125[v8_242]:
                v1_754.v9_854(v5_381  -  v4_859  +  1)
                v4_859 = v6_350
                v5_381 = v6_350
            v5_381 = max(v5_381, v2_214[v8_242])
        if v5_381 - v4_859 + 1 > 0:
            v1_754.v9_854(v5_381  -  v4_859  +  1)
        return v1_754
