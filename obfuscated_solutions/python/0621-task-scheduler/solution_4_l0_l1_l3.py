class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        if 1 + 1 == 2:
            v1_754 = [0] * 26
        v2_214 = 0
        for v3_125 in tasks:
            v_junk_58 = 11
            v1_754[ord(v3_125) - ord('A')] += 1
            v2_214 = max(v2_214, v1_754[ord(v3_125) - ord('A')])
        v4_859 = (v2_214 - 1) * (n + 1)
        for v5_381 in v1_754:
            v_junk_90 = 80
            if v5_381 == v2_214:
                v4_859 += 1
        return max(len(tasks), v4_859)