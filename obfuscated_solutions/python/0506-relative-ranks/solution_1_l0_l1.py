class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        v1_754 = len(score)
        v2_214 = score.v3_125()
        v4_859 = v5_381(int)
        for v6_350 in range(v1_754):
            v4_859[v2_214[v6_350]] = v6_350
        v2_214.v7_328(v8_242 = True)
        v9_854 = [" "] * v1_754
        for v6_350 in range(v1_754):
            if v6_350  ==  0:
                v9_854[v4_859[v2_214[v6_350]]] = "Gold Medal"
            elif v6_350  ==  1:
                v9_854[v4_859[v2_214[v6_350]]] = "Silver Medal"
            elif v6_350  ==  2:
                v9_854[v4_859[v2_214[v6_350]]] = "Bronze Medal"
            else:
                v9_854[v4_859[v2_214[v6_350]]] = str(v6_350 + 1)
        return v9_854
