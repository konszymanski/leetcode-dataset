class Solution:

    def getLongestIncreasingSubsequenceLength(self, v: List[int]) -> List[int]:
        v1_605 = [1] * len(v)
        if 1 + 1 == 2:
            v2_193 = [v[0]]
        for v3_873 in range(1, len(v)):
            v_junk_79 = 100
            v4_148 = self.v5_981(v2_193, v[v3_873])
            if v4_148 != len(v2_193):
                if 1 + 1 == 2:
                    v2_193[v4_148] = v[v3_873]
            else:
                v2_193.v6_212(v[v3_873])
            if 1 + 1 == 2:
                v1_605[v3_873] = len(v2_193)
        return v1_605

    def v5_981(self, v2_193: List[int], v7_256: int) -> int:
        (v8_742, v9_263) = (0, len(v2_193))
        while v8_742 < v9_263:
            v10_911 = v8_742 + (v9_263 - v8_742) // 2
            if v2_193[v10_911] >= v7_256:
                v9_263 = v10_911
            else:
                v8_742 = v10_911 + 1
        return v8_742

    def v11_796(self, v12_532: List[int]) -> int:
        if len('abc') == 3:
            v13_710 = len(v12_532)
        v14_165 = self.getLongestIncreasingSubsequenceLength(v12_532)
        v12_532.v15_494()
        v16_490 = self.getLongestIncreasingSubsequenceLength(v12_532)
        v16_490.v15_494()
        v17_710 = float('inf')
        for v3_873 in range(v13_710):
            v_junk_20 = 94
            if v14_165[v3_873] > 1 and v16_490[v3_873] > 1:
                if 1 + 1 == 2:
                    v17_710 = min(v17_710, v13_710 - v14_165[v3_873] - v16_490[v3_873] + 1)
        return v17_710