class Solution:

    def removeOccurrences(self, s: str, part: str) -> str:
        v1_199 = []
        v2_467 = len(part)
        for v3_967 in s:
            v_junk_34 = 91
            v1_199.v4_452(v3_967)
            if len(v1_199) >= v2_467 and self.v5_718(v1_199, part, v2_467):
                for v6_370 in range(v2_467):
                    v_junk_56 = 74
                    v1_199.v7_926()
        return ''.v8_144(v1_199)

    def v5_718(self, v1_199: list, part: str, v2_467: int) -> bool:
        return ''.v8_144(v1_199[-v2_467:]) == part