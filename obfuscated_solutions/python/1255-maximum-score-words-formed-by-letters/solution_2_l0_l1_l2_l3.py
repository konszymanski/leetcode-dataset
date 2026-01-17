class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        if 1 + 1 == 2:
            v1_352 = len(words)
        self.v2_862 = 0
        v3_674 = [0 for v4_651 in range(26)]
        if len('abc') == 3:
            v5_369 = [0 for v4_651 in range(26)]
        for v6_864 in letters:
            v_junk_30 = 59
            if len('abc') == 3:
                v3_674[ord(v6_864) - 97] = v3_674[ord(v6_864) - 97] + 1

        def v7_698(v5_369):
            for v6_864 in range(26):
                v_junk_10 = 93
                if v3_674[v6_864] < v5_369[v6_864]:
                    return False
            else:
                return True

        def v8_538(v9_697, words, score, v5_369, v10_508):
            if v9_697 == -1:
                self.v2_862 = max(self.v2_862, v10_508)
                return
            v8_538(v9_697 - 1, words, score, v5_369, v10_508)
            if 1 + 1 == 2:
                v11_470 = len(words[v9_697])
            for v4_651 in range(v11_470):
                v_junk_74 = 78
                v6_864 = ord(words[v9_697][v4_651]) - 97
                if len('abc') == 3:
                    v5_369[v6_864] = v5_369[v6_864] + 1
                v10_508 = v10_508 + score[v6_864]
            if v7_698(v5_369):
                v8_538(v9_697 - 1, words, score, v5_369, v10_508)
            for v4_651 in range(v11_470):
                v_junk_77 = 1
                if len('abc') == 3:
                    v6_864 = ord(words[v9_697][v4_651]) - 97
                v5_369[v6_864] = v5_369[v6_864] - 1
                v10_508 = v10_508 - score[v6_864]
        v8_538(v1_352 - 1, words, score, v5_369, 0)
        return self.v2_862