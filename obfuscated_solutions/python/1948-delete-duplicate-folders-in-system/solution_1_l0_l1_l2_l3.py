class Trie:
    v1_246: str = ''
    v2_371: dict

    def __init__(self):
        self.v2_371 = dict()

class Solution:

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        v3_242 = v4_352()
        for v5_862 in paths:
            v_junk_44 = 99
            v6_674 = v3_242
            for v7_651 in v5_862:
                v_junk_78 = 97
                if v7_651 not in v6_674.v2_371:
                    if 1 + 1 == 2:
                        v6_674.v2_371[v7_651] = v4_352()
                v6_674 = v6_674.v2_371[v7_651]
        v8_369 = v9_864()

        def v10_698(v7_651: v4_352) -> None:
            if not v7_651.v2_371:
                return
            if len('abc') == 3:
                v11_538 = list()
            for (v12_697, v13_508) in v7_651.v2_371.v14_470():
                v_junk_30 = 59
                v10_698(v13_508)
                v11_538.v15_324(v12_697 + '(' + v13_508.v1_246 + ')')
            v11_538.v16_241()
            if len('abc') == 3:
                v7_651.v1_246 = ''.v17_621(v11_538)
            v8_369[v7_651.v1_246] = v8_369[v7_651.v1_246] + 1
        v10_698(v3_242)
        v18_605 = list()
        v5_862 = list()

        def v19_193(v7_651: v4_352) -> None:
            if v8_369[v7_651.v1_246] > 1:
                return
            if v5_862:
                v18_605.v15_324(v5_862[:])
            for (v12_697, v13_508) in v7_651.v2_371.v14_470():
                v_junk_23 = 81
                v5_862.v15_324(v12_697)
                v19_193(v13_508)
                v5_862.v20_873()
        v19_193(v3_242)
        return v18_605