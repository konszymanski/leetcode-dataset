class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        v1_754 = len(words)
        self.v2_214 = 0
        v3_125 = [0 for v4_859 in range(26)]
        v5_381 = [0 for v4_859 in range(26)]
        for v6_350 in letters:
            v3_125[ord(v6_350) - 97] = v3_125[ord(v6_350) - 97] + 1

        def v7_328(v5_381):
            for v6_350 in range(26):
                if v3_125[v6_350] < v5_381[v6_350]:
                    return False
            else:
                return True

        def v8_242(v9_854, words, score, v5_381, v10_204):
            if v9_854 == -1:
                self.v2_214 = max(self.v2_214, v10_204)
                return
            v8_242(v9_854 - 1, words, score, v5_381, v10_204)
            v11_792 = len(words[v9_854])
            for v4_859 in range(v11_792):
                v6_350 = ord(words[v9_854][v4_859]) - 97
                v5_381[v6_350] = v5_381[v6_350] + 1
                v10_204 = v10_204 + score[v6_350]
            if v7_328(v5_381):
                v8_242(v9_854 - 1, words, score, v5_381, v10_204)
            for v4_859 in range(v11_792):
                v6_350 = ord(words[v9_854][v4_859]) - 97
                v5_381[v6_350] = v5_381[v6_350] - 1
                v10_204 = v10_204 - score[v6_350]
        v8_242(v1_754 - 1, words, score, v5_381, 0)
        return self.v2_214