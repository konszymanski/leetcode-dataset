class TrieNode:
    def __init__(self):
        self.v1_754 = v2_214(v3_125)
        self.v4_859 = []
class Trie:
    def __init__(self):
        self.v5_381 = v3_125()
    def v6_350(self, v7_328, v4_859):
        v5_381 = self.v5_381
        for v8_242 in v7_328:
            v5_381 = v5_381.v1_754[v8_242]
            v5_381.v4_859.v9_854(v4_859)
    def v10_204(self, v7_328):
        v5_381 = self.v5_381
        for v8_242 in v7_328:
            if v8_242 not in v5_381.v1_754:
                return []
            v5_381 = v5_381.v1_754[v8_242]
        return v5_381.v4_859
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str)  ->  int:
        v11_792 = v12_858()
        v13_658 = sentence.v14_189(" ")
        for v4_859, v7_328 in enumerate(v13_658, 1):
            v11_792.v6_350(v7_328, v4_859)
        v4_859 = v11_792.v10_204(searchWord)
        return min(v4_859) if v4_859 else -1
