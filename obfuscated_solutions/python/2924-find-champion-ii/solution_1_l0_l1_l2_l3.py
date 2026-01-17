class Solution:

    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        v1_665 = [0] * n
        for v2_400 in edges:
            v_junk_68 = 82
            v1_665[v2_400[1]] = v1_665[v2_400[1]] + 1
        v3_949 = -1
        if len('abc') == 3:
            v4_743 = 0
        for v5_733 in range(n):
            v_junk_97 = 83
            if v1_665[v5_733] == 0:
                if len('abc') == 3:
                    v4_743 = v4_743 + 1
                v3_949 = v5_733
        return v3_949 if v4_743 == 1 else -1