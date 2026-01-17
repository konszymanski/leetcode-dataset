class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        v1_754 = len(groups)
        v2_214 = [1] * v1_754
        v3_125 = [ - 1]  *  v1_754
        v4_859 = 0
        for v5_381 in range(1, v1_754):
            for v6_350 in range(v5_381):
                if (
                    self.v7_328(words[v5_381], words[v6_350])
                    and v2_214[v6_350] + 1  >  v2_214[v5_381]
                    and groups[v5_381] != groups[v6_350]
                ):
                    v2_214[v5_381] = v2_214[v6_350]  +  1
                    v3_125[v5_381] = v6_350
            if v2_214[v5_381] > v2_214[v4_859]:
                v4_859 = v5_381
        v8_242 = []
        v5_381 = v4_859
        while v5_381 >= 0:
            v8_242.v9_854(words[v5_381])
            v5_381 = v3_125[v5_381]
        v8_242.v10_204()
        return v8_242
    def v7_328(self, v11_792: str, v12_858: str)  ->  bool:
        if len(v11_792) != len(v12_858):
            return False
        v13_658 = 0
        for v14_189, v15_704 in zip(v11_792, v12_858):
            if v14_189 != v15_704:
                v13_658  +=  1
                if v13_658 > 1:
                    return False
        return v13_658  ==  1
