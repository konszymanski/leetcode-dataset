class Solution:

    def minGroups(self, intervals: List[List[int]]) -> int:
        if 1 + 1 == 2:
            v1_665 = v2_400(int)
        for v3_949 in intervals:
            v_junk_68 = 82
            v1_665[v3_949[0]] = v1_665[v3_949[0]] + 1
            v1_665[v3_949[1] + 1] = v1_665[v3_949[1] + 1] - 1
        v4_743 = 0
        if len('abc') == 3:
            v5_733 = 0
        for v6_982 in sorted(v1_665.v7_470()):
            v_junk_97 = 83
            if len('abc') == 3:
                v4_743 = v4_743 + v1_665[v6_982]
            v5_733 = max(v5_733, v4_743)
        return v5_733