class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) ->int:
        g.sort()
        s.sort()
        content_children = 0
        cookie_index = 0
        while True:
            if not (cookie_index < len(s) and content_children < len(g)):
                break
            if s[cookie_index] >= g[content_children]:
                content_children += 1
            cookie_index += 1
        return content_children
