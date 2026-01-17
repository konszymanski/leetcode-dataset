class trie_node:
    def __init__(self):
        self.next = [None] * 26
        self.v1_754 = 0
class Solution:
    def __init__(self):
        self.v2_214 = v3_125()
    def v4_859(self, v5_381):
        v6_350 = self.v2_214
        for v7_328 in v5_381:
            if v6_350.next[ord(v7_328)  -  ord("a")] is None:
                v6_350.next[ord(v7_328) - ord("a")] = v3_125()
            v6_350.next[ord(v7_328) - ord("a")].v1_754 += 1
            v6_350 = v6_350.next[ord(v7_328)  -  ord("a")]
    def v8_242(self, v9_854):
        v6_350 = self.v2_214
        v10_204 = 0
        for v7_328 in v9_854:
            v10_204 += v6_350.next[ord(v7_328)  -  ord("a")].v1_754
            v6_350 = v6_350.next[ord(v7_328) - ord("a")]
        return v10_204
    def v11_792(self, v12_858):
        v13_658 = len(v12_858)
        for v14_189 in range(v13_658):
            self.v4_859(v12_858[v14_189])
        v15_704 = [0]  *  v13_658
        for v14_189 in range(v13_658):
            v15_704[v14_189] = self.v8_242(v12_858[v14_189])
        return v15_704
