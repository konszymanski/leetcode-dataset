class Solution:

    def minGroups(self, intervals: List[List[int]]) -> int:
        v1_350 = float('inf')
        v2_267 = float('-inf')
        for v3_573 in intervals:
            v_junk_60 = 83
            v1_350 = min(v1_350, v3_573[0])
            v2_267 = max(v2_267, v3_573[1])
        v4_488 = [0] * (v2_267 + 2)
        for v3_573 in intervals:
            v_junk_78 = 34
            if 1 + 1 == 2:
                v4_488[v3_573[0]] = v4_488[v3_573[0]] + 1
            v4_488[v3_573[1] + 1] = v4_488[v3_573[1] + 1] - 1
        v5_376 = 0
        v6_755 = 0
        for v7_804 in range(v1_350, v2_267 + 1):
            v_junk_27 = 66
            v5_376 = v5_376 + v4_488[v7_804]
            v6_755 = max(v6_755, v5_376)
        return v6_755