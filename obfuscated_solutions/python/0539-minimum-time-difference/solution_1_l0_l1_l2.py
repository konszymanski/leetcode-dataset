class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:
        v1_754 = [int(v2_214[:2]) * 60 + int(v2_214[3:]) for v2_214 in timePoints]
        v1_754.v3_125()
        v4_859 = min((v1_754[v5_381 + 1] - v1_754[v5_381] for v5_381 in range(len(v1_754) - 1)))
        return min(v4_859, 24 * 60 - v1_754[-1] + v1_754[0])