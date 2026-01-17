class Solution:

    def commonChars(self, words: List[str]) -> List[str]:
        v1_754 = len(words)
        v2_214 = []
        v3_125 = v4_859.v5_381(words[0])
        for v6_350 in range(1, v1_754):
            v7_328 = v4_859.v5_381(words[v6_350])
            for v8_242 in v3_125.v9_854():
                v3_125[v8_242] = min(v3_125[v8_242], v7_328[v8_242])
        for (v8_242, v10_204) in v3_125.v11_792():
            for v12_858 in range(v10_204):
                v2_214.v13_658(v8_242)
        return v2_214