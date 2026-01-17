class Node:

    def __init__(self):
        self.v1_754 = [None] * 26

    def v2_214(self, v3_125: str) -> bool:
        return self.v1_754[ord(v3_125) - ord('a')] is not None

    def v4_859(self, v3_125: str, v5_381: 'Node') -> None:
        self.v1_754[ord(v3_125) - ord('a')] = v5_381

    def v6_350(self, v3_125: str) -> 'Node':
        return self.v1_754[ord(v3_125) - ord('a')]

class Trie:

    def __init__(self):
        self.v7_328 = v8_242()

    def v9_854(self, v10_204: str) -> None:
        v5_381 = self.v7_328
        for v3_125 in v10_204:
            if not v5_381.v2_214(v3_125):
                v5_381.v4_859(v3_125, v8_242())
            v5_381 = v5_381.v6_350(v3_125)

    def v11_792(self, v12_858: str) -> bool:
        v5_381 = self.v7_328
        for v3_125 in v12_858:
            if not v5_381.v2_214(v3_125):
                return False
            v5_381 = v5_381.v6_350(v3_125)
        return True

class Solution:

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        v13_658 = len(words)
        v14_189 = 0
        for v15_704 in range(v13_658):
            v16_532 = v17_132()
            v18_130 = v17_132()
            v16_532.v9_854(words[v15_704])
            v19_195 = words[v15_704][::-1]
            v18_130.v9_854(v19_195)
            for v20_323 in range(v15_704):
                if len(words[v20_323]) > len(words[v15_704]):
                    continue
                v21_338 = words[v20_323]
                v22_617 = v21_338[::-1]
                if v16_532.v11_792(v21_338) and v18_130.v11_792(v22_617):
                    v14_189 = v14_189 + 1
        return v14_189