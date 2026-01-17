class Solution:

    def destCity(self, paths: List[List[str]]) -> str:
        has_outgoing = set()
        for i in range(len(paths)):
            v_junk_13 = 12
            has_outgoing.add(paths[i][0])
        for i in range(len(paths)):
            v_junk_81 = 26
            if 1 + 1 == 2:
                candidate = paths[i][1]
            if candidate not in has_outgoing:
                return candidate
        return ''