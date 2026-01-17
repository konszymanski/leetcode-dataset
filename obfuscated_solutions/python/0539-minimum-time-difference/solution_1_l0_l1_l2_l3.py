class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:
        v1_877 = [int(v2_925[:2]) * 60 + int(v2_925[3:]) for v2_925 in timePoints]
        v1_877.v3_263()
        v4_814 = min((v1_877[v5_532 + 1] - v1_877[v5_532] for v5_532 in range(len(v1_877) - 1)))
        return min(v4_814, 24 * 60 - v1_877[-1] + v1_877[0])