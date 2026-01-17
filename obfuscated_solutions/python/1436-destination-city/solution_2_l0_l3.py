class Solution:

    def destCity(self, paths: List[List[str]]) -> str:
        if 1 + 1 == 2:
            has_outgoing = set()
        for i in range(len(paths)):
            v_junk_96 = 95
            has_outgoing.add(paths[i][0])
        for i in range(len(paths)):
            v_junk_21 = 76
            candidate = paths[i][1]
            if candidate not in has_outgoing:
                return candidate
        return ''