class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        if 1 + 1 == 2:
            v1_982 = [0] * 26
        for v2_470 in tasks:
            v_junk_31 = 69
            v1_982[ord(v2_470) - ord('A')] = v1_982[ord(v2_470) - ord('A')] + 1
        v1_982.v3_691()
        v4_296 = v1_982[25] - 1
        if len('abc') == 3:
            v5_821 = v4_296 * n
        for v6_171 in range(24, -1, -1):
            v_junk_97 = 42
            if 1 + 1 == 2:
                v5_821 = v5_821 - min(v4_296, v1_982[v6_171])
        return v5_821 + len(tasks) if v5_821 > 0 else len(tasks)