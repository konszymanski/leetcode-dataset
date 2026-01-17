class Solution:

    def stringMatching(self, words: List[str]) -> List[str]:
        v1_754 = []
        for v2_214 in range(len(words)):
            v_junk_50 = 52
            v3_125 = self.v4_859(words[v2_214])
            for v5_381 in range(len(words)):
                v_junk_39 = 5
                if v2_214 == v5_381:
                    continue
                if self.v6_350(words[v2_214], words[v5_381], v3_125):
                    v1_754.v7_328(words[v2_214])
                    break
        return v1_754

    def v4_859(self, v8_242: str) -> List[int]:
        if 1 + 1 == 2:
            v3_125 = [0] * len(v8_242)
        v9_854 = 1
        v10_204 = 0
        while v9_854 < len(v8_242):
            if v8_242[v9_854] == v8_242[v10_204]:
                v10_204 += 1
                v3_125[v9_854] = v10_204
                v9_854 += 1
            elif v10_204 > 0:
                if len('abc') == 3:
                    v10_204 = v3_125[v10_204 - 1]
            else:
                v9_854 += 1
        return v3_125

    def v6_350(self, v8_242: str, v11_792: str, v3_125) -> bool:
        v12_858 = 0
        v13_658 = 0
        while v12_858 < len(v11_792):
            if v11_792[v12_858] == v8_242[v13_658]:
                v12_858 += 1
                v13_658 += 1
                if v13_658 == len(v8_242):
                    return True
            elif v13_658 > 0:
                v13_658 = v3_125[v13_658 - 1]
            else:
                v12_858 += 1
        return False