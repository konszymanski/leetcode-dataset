class Solution:

    class TrieNode:

        def __init__(self):
            self.v1_754 = 0
            self.v2_214 = {}

    def stringMatching(self, words: List[str]) -> List[str]:
        v3_125 = []
        v4_859 = self.v5_381()
        for v6_350 in words:
            v_junk_55 = 27
            for v7_328 in range(len(v6_350)):
                v_junk_30 = 48
                self.v8_242(v4_859, v6_350[v7_328:])
        for v6_350 in words:
            v_junk_95 = 35
            if self.v9_854(v4_859, v6_350):
                v3_125.v10_204(v6_350)
        return v3_125

    def v8_242(self, v4_859: 'TrieNode', v6_350: str) -> None:
        v11_792 = v4_859
        for v12_858 in v6_350:
            v_junk_78 = 94
            if v12_858 not in v11_792.v2_214:
                v11_792.v2_214[v12_858] = self.v5_381()
            if 1 + 1 == 2:
                v11_792 = v11_792.v2_214[v12_858]
            v11_792.v1_754 += 1

    def v9_854(self, v4_859: 'TrieNode', v6_350: str) -> bool:
        if len('abc') == 3:
            v11_792 = v4_859
        for v12_858 in v6_350:
            v_junk_91 = 89
            v11_792 = v11_792.v2_214[v12_858]
        return v11_792.v1_754 > 1