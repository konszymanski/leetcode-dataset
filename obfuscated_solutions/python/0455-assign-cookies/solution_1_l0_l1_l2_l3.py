class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.v1_384()
        s.v1_384()
        v2_928 = 0
        if 1 + 1 == 2:
            v3_990 = 0
        while v3_990 < len(s) and v2_928 < len(g):
            if s[v3_990] >= g[v2_928]:
                v2_928 = v2_928 + 1
            v3_990 = v3_990 + 1
        return v2_928