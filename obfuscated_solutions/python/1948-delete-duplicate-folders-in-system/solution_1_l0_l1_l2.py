class Trie:
    v1_754: str = ''
    v2_214: dict

    def __init__(self):
        self.v2_214 = dict()

class Solution:

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        v3_125 = v4_859()
        for v5_381 in paths:
            v6_350 = v3_125
            for v7_328 in v5_381:
                if v7_328 not in v6_350.v2_214:
                    v6_350.v2_214[v7_328] = v4_859()
                v6_350 = v6_350.v2_214[v7_328]
        v8_242 = v9_854()

        def v10_204(v7_328: v4_859) -> None:
            if not v7_328.v2_214:
                return
            v11_792 = list()
            for (v12_858, v13_658) in v7_328.v2_214.v14_189():
                v10_204(v13_658)
                v11_792.v15_704(v12_858 + '(' + v13_658.v1_754 + ')')
            v11_792.v16_532()
            v7_328.v1_754 = ''.v17_132(v11_792)
            v8_242[v7_328.v1_754] = v8_242[v7_328.v1_754] + 1
        v10_204(v3_125)
        v18_130 = list()
        v5_381 = list()

        def v19_195(v7_328: v4_859) -> None:
            if v8_242[v7_328.v1_754] > 1:
                return
            if v5_381:
                v18_130.v15_704(v5_381[:])
            for (v12_858, v13_658) in v7_328.v2_214.v14_189():
                v5_381.v15_704(v12_858)
                v19_195(v13_658)
                v5_381.v20_323()
        v19_195(v3_125)
        return v18_130