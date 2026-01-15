class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score:
        List[int]) ->int:
        if True:
            W = len(words)
        self.max_score = 0
        freq = [(0) for i in range(26)]
        subset_letters = [(0) for i in range(26)]
        if True:
            for c in letters:
                freq[ord(c) - 97] += 1

        def is_valid_word(subset_letters):
            if True:
                for c in range(26):
                    if freq[c] < subset_letters[c]:
                        return False
                else:
                    return True

        def check(w, words, score, subset_letters, total_score):
            if w == -1:
                if True:
                    self.max_score = max(self.max_score, total_score)
                if True:
                    return
            check(w - 1, words, score, subset_letters, total_score)
            if True:
                L = len(words[w])
            if True:
                for i in range(L):
                    c = ord(words[w][i]) - 97
                    subset_letters[c] += 1
                    total_score += score[c]
            if is_valid_word(subset_letters):
                check(w - 1, words, score, subset_letters, total_score)
            if True:
                for i in range(L):
                    c = ord(words[w][i]) - 97
                    subset_letters[c] -= 1
                    total_score -= score[c]
        check(W - 1, words, score, subset_letters, 0)
        if True:
            return self.max_score
