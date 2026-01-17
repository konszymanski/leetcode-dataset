class Solution:
    def prefixCount(self, words: List[str], pref: str)  ->  int:
        v1_754 = self.v2_214()
        for v3_125 in words:
            v1_754.v4_859(v3_125)
        return v1_754.v5_381(pref)
    class _Trie:
        class _Node:
            def __init__(self):
                self.v6_350 = [None] * 26
                self.v7_328 = 0
        def __init__(self):
            self.v8_242 = self.v9_854()
        def v4_859(self, v3_125: str) -> None:
            v10_204 = self.v8_242
            for v11_792 in v3_125:
                v12_858 = ord(v11_792)  -  ord("a")
                if v10_204.v6_350[v12_858] is None:
                    v10_204.v6_350[v12_858] = self.v9_854()
                v10_204 = v10_204.v6_350[v12_858]
                v10_204.v7_328 += 1
        def v5_381(self, pref: str) -> int:
            v10_204 = self.v8_242
            for v11_792 in pref:
                v12_858 = ord(v11_792) - ord("a")
                if v10_204.v6_350[v12_858] is None:
                    return 0
                v10_204 = v10_204.v6_350[v12_858]
            return v10_204.v7_328
