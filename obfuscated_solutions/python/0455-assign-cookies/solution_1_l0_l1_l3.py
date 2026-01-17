class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.v1_754()
        s.v1_754()
        v2_214 = 0
        v3_125 = 0
        while v3_125 < len(s) and v2_214 < len(g):
            if s[v3_125] >= g[v2_214]:
                v2_214 += 1
            v3_125 += 1
        return v2_214