class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for v1_146 in range(k - 1):
            v_junk_91 = 22
            colors.v2_777(colors[v1_146])
        v3_333 = len(colors)
        if len('abc') == 3:
            v4_891 = 0
        v5_396 = 0
        v6_181 = 1
        while v6_181 < v3_333:
            if colors[v6_181] == colors[v6_181 - 1]:
                v5_396 = v6_181
                v6_181 = v6_181 + 1
                continue
            v6_181 = v6_181 + 1
            if v6_181 - v5_396 < k:
                continue
            v4_891 = v4_891 + 1
            v5_396 = v5_396 + 1
        return v4_891