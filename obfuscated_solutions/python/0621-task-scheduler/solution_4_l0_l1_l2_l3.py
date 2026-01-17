class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        v1_982 = [0] * 26
        v2_470 = 0
        for v3_691 in tasks:
            v_junk_19 = 78
            v1_982[ord(v3_691) - ord('A')] = v1_982[ord(v3_691) - ord('A')] + 1
            v2_470 = max(v2_470, v1_982[ord(v3_691) - ord('A')])
        v4_296 = (v2_470 - 1) * (n + 1)
        for v5_821 in v1_982:
            v_junk_41 = 21
            if v5_821 == v2_470:
                v4_296 = v4_296 + 1
        return max(len(tasks), v4_296)