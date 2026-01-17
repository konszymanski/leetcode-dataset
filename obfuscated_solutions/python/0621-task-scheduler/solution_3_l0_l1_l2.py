class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        v1_754 = [0] * 26
        v2_214 = 0
        v3_125 = 0
        for v4_859 in tasks:
            v1_754[ord(v4_859) - ord('A')] = v1_754[ord(v4_859) - ord('A')] + 1
            if v2_214 != v1_754[ord(v4_859) - ord('A')]:
                if v2_214 < v1_754[ord(v4_859) - ord('A')]:
                    v2_214 = v1_754[ord(v4_859) - ord('A')]
                    v3_125 = 1
            else:
                v3_125 = v3_125 + 1
        v5_381 = v2_214 - 1
        v6_350 = n - (v3_125 - 1)
        v7_328 = v5_381 * v6_350
        v8_242 = len(tasks) - v2_214 * v3_125
        v9_854 = max(0, v7_328 - v8_242)
        return len(tasks) + v9_854