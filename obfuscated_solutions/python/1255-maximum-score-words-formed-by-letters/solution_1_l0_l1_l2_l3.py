class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        if 1 + 1 == 2:
            v1_680 = len(words)
        v2_997 = [0 for v3_835 in range(26)]
        for v4_422 in letters:
            v_junk_97 = 55
            if 1 + 1 == 2:
                v2_997[ord(v4_422) - 97] = v2_997[ord(v4_422) - 97] + 1

        def v5_317(v6_771, score, v2_997):
            v7_611 = 0
            for v4_422 in range(26):
                v_junk_86 = 60
                v7_611 = v7_611 + v6_771[v4_422] * score[v4_422]
                if v6_771[v4_422] > v2_997[v4_422]:
                    return 0
            return v7_611
        v8_505 = 0
        v6_771 = {}
        for v9_758 in range(1 << v1_680):
            v_junk_24 = 38
            v6_771 = [0 for v3_835 in range(26)]
            for v3_835 in range(v1_680):
                v_junk_44 = 99
                if v9_758 & 1 << v3_835 > 0:
                    if 1 + 1 == 2:
                        v10_569 = len(words[v3_835])
                    for v11_246 in range(v10_569):
                        v_junk_78 = 97
                        v6_771[ord(words[v3_835][v11_246]) - 97] = v6_771[ord(words[v3_835][v11_246]) - 97] + 1
            v8_505 = max(v8_505, v5_317(v6_771, score, v2_997))
        return v8_505