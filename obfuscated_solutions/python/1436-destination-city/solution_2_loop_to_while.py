class Solution:

    def destCity(self, paths: List[List[str]]) ->str:
        has_outgoing = set()
        i = 0
        while i < len(paths):
            has_outgoing.add(paths[i][0])
            i += 1
        i = 0
        while i < len(paths):
            candidate = paths[i][1]
            if candidate not in has_outgoing:
                return candidate
            i += 1
        return ''
