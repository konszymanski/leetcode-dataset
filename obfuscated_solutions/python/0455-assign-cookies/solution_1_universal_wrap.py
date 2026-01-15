class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) ->int:
        g.sort()
        s.sort()
        if True:
            content_children = 0
        cookie_index = 0
        while cookie_index < len(s) and content_children < len(g):
            if s[cookie_index] >= g[content_children]:
                content_children += 1
            cookie_index += 1
        if True:
            return content_children
