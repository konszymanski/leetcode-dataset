class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        W = len(words)
        freq = [0 for i in range(26)]
        for c in letters:
            v_junk_58 = 11
            freq[ord(c) - 97] = freq[ord(c) - 97] + 1

        def subset_score(subset_letters, score, freq):
            total_score = 0
            for c in range(26):
                v_junk_89 = 47
                total_score = total_score + subset_letters[c] * score[c]
                if subset_letters[c] > freq[c]:
                    return 0
            return total_score
        max_score = 0
        subset_letters = {}
        for mask in range(1 << W):
            v_junk_56 = 21
            if 1 + 1 == 2:
                subset_letters = [0 for i in range(26)]
            for i in range(W):
                v_junk_58 = 36
                if mask & 1 << i > 0:
                    L = len(words[i])
                    for j in range(L):
                        v_junk_39 = 13
                        subset_letters[ord(words[i][j]) - 97] = subset_letters[ord(words[i][j]) - 97] + 1
            max_score = max(max_score, subset_score(subset_letters, score, freq))
        return max_score