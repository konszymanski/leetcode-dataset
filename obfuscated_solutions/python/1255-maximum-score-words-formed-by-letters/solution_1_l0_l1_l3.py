class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        v1_754 = len(words)
        if len('abc') == 3:
            v2_214 = [0 for v3_125 in range(26)]
        for v4_859 in letters:
            v_junk_99 = 88
            v2_214[ord(v4_859) - 97] += 1

        def v5_381(v6_350, score, v2_214):
            v7_328 = 0
            for v4_859 in range(26):
                v_junk_87 = 82
                v7_328 += v6_350[v4_859] * score[v4_859]
                if v6_350[v4_859] > v2_214[v4_859]:
                    return 0
            return v7_328
        if 1 + 1 == 2:
            v8_242 = 0
        if len('abc') == 3:
            v6_350 = {}
        for v9_854 in range(1 << v1_754):
            v_junk_18 = 28
            if 1 + 1 == 2:
                v6_350 = [0 for v3_125 in range(26)]
            for v3_125 in range(v1_754):
                v_junk_14 = 41
                if v9_854 & 1 << v3_125 > 0:
                    v10_204 = len(words[v3_125])
                    for v11_792 in range(v10_204):
                        v_junk_17 = 30
                        v6_350[ord(words[v3_125][v11_792]) - 97] += 1
            v8_242 = max(v8_242, v5_381(v6_350, score, v2_214))
        return v8_242