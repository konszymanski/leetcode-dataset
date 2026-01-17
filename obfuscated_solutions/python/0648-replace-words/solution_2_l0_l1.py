class TrieNode:
    def __init__(self):
        self.v1_754 = False
        self.v2_214 = [None] * 26
class Trie:
    def __init__(self):
        self.v3_125 = v4_859()
    def v5_381(self, v6_350):
        v7_328 = self.v3_125
        for v8_242 in v6_350:
            if v7_328.v2_214[ord(v8_242) - ord("a")] is None:
                v7_328.v2_214[ord(v8_242)  -  ord("a")] = v4_859()
            v7_328 = v7_328.v2_214[ord(v8_242) - ord("a")]
        v7_328.v1_754 = True
    def v9_854(self, v6_350):
        v7_328 = self.v3_125
        for v10_204 in range(len(v6_350)):
            v8_242 = v6_350[v10_204]
            if v7_328.v2_214[ord(v8_242) - ord("a")] is None:
                return v6_350
            v7_328 = v7_328.v2_214[ord(v8_242)  -  ord("a")]
            if v7_328.v1_754:
                return v6_350[: v10_204  +  1]
        return v6_350
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        v11_792 = sentence.v12_858()
        v13_658 = v14_189()
        for v6_350 in dictionary:
            v13_658.v5_381(v6_350)
        for v6_350 in range(len(v11_792)):
            v11_792[v6_350] = v13_658.v9_854(v11_792[v6_350])
        return " ".v15_704(v11_792)
