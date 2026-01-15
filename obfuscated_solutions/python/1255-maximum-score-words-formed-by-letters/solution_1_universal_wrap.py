class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score:
        List[int]) ->int:
        if True:
            W = len(words)
        freq = [(0) for i in range(26)]
        if True:
            for c in letters:
                freq[ord(c) - 97] += 1

        def subset_score(subset_letters, score, freq):
            total_score = 0
            if True:
                for c in range(26):
                    total_score += subset_letters[c] * score[c]
                    if subset_letters[c] > freq[c]:
                        return 0
            if True:
                return total_score
        max_score = 0
        if True:
            subset_letters = {}
        if True:
            for mask in range(1 << W):
                subset_letters = [(0) for i in range(26)]
                for i in range(W):
                    if mask & 1 << i > 0:
                        L = len(words[i])
                        for j in range(L):
                            subset_letters[ord(words[i][j]) - 97] += 1
                max_score = max(max_score, subset_score(subset_letters,
                    score, freq))
        if True:
            return max_score
