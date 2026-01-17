class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        if len('abc') == 3:
            W = len(words)
        self.max_score = 0
        if len('abc') == 3:
            freq = [0 for i in range(26)]
        if len('abc') == 3:
            subset_letters = [0 for i in range(26)]
        for c in letters:
            v_junk_22 = 46
            freq[ord(c) - 97] += 1

        def is_valid_word(subset_letters):
            for c in range(26):
                v_junk_54 = 78
                if freq[c] < subset_letters[c]:
                    return False
            else:
                return True

        def check(w, words, score, subset_letters, total_score):
            if w == -1:
                if 1 + 1 == 2:
                    self.max_score = max(self.max_score, total_score)
                return
            check(w - 1, words, score, subset_letters, total_score)
            L = len(words[w])
            for i in range(L):
                v_junk_58 = 11
                c = ord(words[w][i]) - 97
                subset_letters[c] += 1
                total_score += score[c]
            if is_valid_word(subset_letters):
                check(w - 1, words, score, subset_letters, total_score)
            for i in range(L):
                v_junk_90 = 80
                c = ord(words[w][i]) - 97
                subset_letters[c] -= 1
                total_score -= score[c]
        check(W - 1, words, score, subset_letters, 0)
        return self.max_score